from django.dispatch import receiver
from django_q.signals import pre_enqueue, pre_execute
from django.db.models.signals import pre_save


@receiver(pre_enqueue)
def pre_enqueue_callback(sender, task, **kwargs):
    # put in queue ?
    print(f"Task {task['name']} will be enqueued")


@receiver(pre_execute)
def pre_execute_callback(sender, func, task, **kwargs):
    # put in the running category
    print(f"Task {task['name']} will be executed by calling {func}")


@receiver(pre_save)
def pre_save_callback(sender, **kwargs):
    # put in the running category
    print(f"pre_save_callback from  {sender}")