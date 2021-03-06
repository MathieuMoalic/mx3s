import os
import subprocess
import multiprocessing
import glob
import time
import sys

import ftpretty

server_ip = '150.254.111.83'
ftp_username = 'client'
ftp_password = '247uT8xdA5uYpq'
ftp_port = 38388
gpus = 2
mumax_ports = [35367, 35368]
home_dir = "/mnt/g/Mathieu/simulations/jimmy/client"


def ftp_put(mumax_subprocesses):
    # _, ip, port, username, password = sys.argv
    f = ftpretty.ftpretty(server_ip, ftp_username, ftp_password, port=ftp_port)
    while True:
        for i, mumax_subprocess in enumerate(mumax_subprocesses):
            mumax_subprocess.poll()
            if mumax_subprocess.returncode is not None:
                finished_sim = mumax_subprocess.args[1]
                print(f"Simulation :{finished_sim} has finished")
                finished_sim_folder = f"{finished_sim[:-3]}out"
                print(f"Cleaning the folder :{finished_sim_folder}")
                meta_files = glob.glob(f"{finished_sim_folder}/*")
                for meta_file in meta_files:
                    f.put(meta_file, meta_file)
                    os.remove(meta_file)
                    print(f"Moved :{meta_file}")
                mumax_subprocesses.pop(i)
                os.rmdir(finished_sim_folder)
            break

        send_queue = glob.glob(f"{home_dir}**/*.ovf")
        for ovf_file in send_queue:
            f.put(ovf_file, ovf_file)
            os.remove(ovf_file)
            print(f"Moved {ovf_file}")
        time.sleep(0.5)


def ssh_tunneling():
    pass


def main():
    free_gpu = [True for i in range(gpus)]
    try:
        simulations_started = []
        mumax_subprocesses = []
        ftp_put_process = multiprocessing.Process(target=ftp_put,
                                                  args=[mumax_subprocesses])
        ftp_put_process.start()

        ssh_tunneling_process = multiprocessing.Process(target=ssh_tunneling)
        ssh_tunneling_process.start()
        while True:
            scipts = glob.glob(f"{home_dir}queued_scripts/*.mx3")
            if any(free_gpu):
                for script in scipts:
                    if script not in simulations_started:
                        print(f"Starting {script} on gpu {gpu}")
                        gpu = free_gpu.index(True)
                        mumax_port = mumax_ports[gpu]
                        s = subprocess.Popen([
                            "mumax3", script, "-gpu", gpu, "-http", mumax_port
                        ],
                                             stdout=subprocess.DEVNULL)
                        mumax_subprocesses.append(s)
                        simulations_started.append(script)
            time.sleep(2)
    except KeyboardInterrupt:
        print("Exiting ...")
        for s in mumax_subprocesses:
            s.kill()
        print("Mumax simulations stopped.")
        ftp_put_process.terminate()
        print("FTP connection closed.")
        ssh_tunneling_process.terminate()
        print("SSH connection closed.")
        sys.exit(0)


if __name__ == "__main__":
    main()
