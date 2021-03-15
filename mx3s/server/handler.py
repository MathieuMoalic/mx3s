import multiprocessing
from time import sleep
from glob import glob
import os
from .models import Simulation

def scan_sims():
    while True:
        queued_sims = [x.split("/")[-1][:-4] for x in glob("/jimmy/queued/*.mx3")]
        running_sims = [x.split("/")[-1][:-4] for x in glob("/jimmy/running/*.out")]
        finished_sims = [x.split("/")[-1][:-4] for x in glob("/jimmy/finished/*.out")]
        print(queued_sims,running_sims,finished_sims)
        for s in Simulation.objects.all():
            print(s.name,s.is_queued,s.is_running,s.is_finished)
        
        for s in Simulation.objects.filter(is_queued=True):
            if s.name in running_sims:
                print(s.name,"is running")
                s.is_queued = False
                s.is_running = True
                s.save()
        for s in Simulation.objects.filter(is_running=True):
            print(s.name)
            if s.name in finished_sims:
                print(s.name,"is finished")
                s.is_queued = False
                s.is_running = False
                s.is_finished = True
                s.save()
        
        sleep(1)

def handler():
    scan_sims_process = multiprocessing.Process(target=scan_sims,
                                                #   stdout="/jimmy/meta/handler.log"
                                                  )
    scan_sims_process.start()