from django.apps import AppConfig as App


class AppConfig(App):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
