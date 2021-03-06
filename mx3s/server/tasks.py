# import django_q.tasks as ta
# import os


# def queue_mumax(form):
#     # print(">>>>>>> queue_mumax")

#     # new_path = form.files.get('script').replace("/mnt/g", "G:").replace('/', '\\')
#     new_path = form.files.get('script').name.replace('/', '\\')
#     new_path = f"U:\\home\\mat\mx3s\\mx3s\\media\\{new_path}"
#     mummax_task = ta.AsyncTask(
#         'subprocess.run',
#         ['/mnt/g/Mathieu/simulations/server/m3/mumax3.exe', new_path],
#         task_name=form.files.get("script").name,
#         group='group1',
#         hook=mumax_sim_finishes)
#     mummax_task.run()


# def mumax_sim_finishes(task):
#     # print(task.result)
#     pass
