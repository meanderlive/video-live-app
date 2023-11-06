from django.apps import AppConfig


class StreamersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'streamers'

    def ready(self):
        import streamers.signals