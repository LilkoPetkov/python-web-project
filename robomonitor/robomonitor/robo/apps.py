from django.apps import AppConfig


class RoboConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'robomonitor.robo'

    def ready(self):
        import celery
