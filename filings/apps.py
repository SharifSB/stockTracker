from django.apps import AppConfig


class FilingsConfig(AppConfig):
    name = 'filings'

    def ready(self):
        from . import updater
        updater.start()