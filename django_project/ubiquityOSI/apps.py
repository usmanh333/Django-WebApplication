from django.apps import AppConfig


class UbiquityosiConfig(AppConfig):
    name = 'ubiquityOSI'


def ready(self):
    import users.signals