from django.apps import AppConfig


class AboutSignalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about_signals'

    def ready(self):
        # we should add our signals here
        import about_signals.signals
