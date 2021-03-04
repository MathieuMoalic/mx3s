# scan a script folder periodically
# start a simulation when a script arrives
# scan folder periodically and send the files to the server
# tell the server when the simulation ends
# repeat

import os
from time import sleep
import subprocess
import shutil
from ftpretty import ftpretty

folder = ""
# folder = "/tmp/g/Mathieu/simulations/test_files"

sim_blacklist = []
f = ftpretty('127.0.0.1', "mat", "123", port=21211)


def main():
    # os.chdir(folder)
    while True:
        scipts = os.listdir()
        print(os.listdir())
        for script in scipts:
            if script[-3:] == "mx3" and script not in sim_blacklist:
                sim_folder = script[:-3] + "out"
                s = subprocess.Popen(["mumax3", script])
                sim_blacklist.append(script)
                sleep(1)
                while True:
                    sim_files = os.listdir(sim_folder)
                    for sim_file in sim_files:
                        if "ovf" in sim_file:
                            # Put a local file into a remote directory, denoted by trailing slash on remote
                            f.put(sim_file, 'simualtions/')
                            os.remove(f"{sim_folder}/{sim_file}")
                            print(f"{script}: removed {sim_file}")
                    s.poll()
                    # print(f"{s.returncode=}")
                    if s.returncode is not None:  # if sim is finished
                        print(f"Simulation :{script} has finished")
                        shutil.rmtree(sim_folder)
                        break
                    sleep(1)
        sleep(2)


if __name__ == "__main__":
    main()