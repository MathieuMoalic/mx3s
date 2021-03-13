import multiprocessing
from time import sleep
from glob import glob
import os
from .models import Simulation,Gpu

def queue_sim(name):
    pass

def scan_sims(queued_sims):
    while True:
        break
        sims = Simulation.objects.filter(is_queued=True)
        print(sims)
        # sims = glob("/home/mat/mx3s/mx3s/media/queued_sims/*.mx3")
        # for sim in sims:
        #     queued_sims.append(sim)
        #     os.rename(sim,)
        sleep(10)

def handler():
    print(">>>>>>>>handler started")
    #keep scanning the simulation folder
    queued_sims = []
    scan_sims_process = multiprocessing.Process(target=scan_sims,
                                                  args=[queued_sims],
                                                #   stdout="/jimmy/meta/handler.log"
                                                  )
    scan_sims_process.start()