from django.apps import AppConfig


class ServerConfig(AppConfig):
    name = 'server'

    # def ready(self):
    #     # registering signals with the model's string label
    #     from .signals import pre_enqueue_callback, pre_execute_callback, pre_save_callback
    #     # pre_save.connect(receiver, sender='app_label.MyModel')