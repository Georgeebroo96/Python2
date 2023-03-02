from django.apps import AppConfig


class TaskprojectappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'taskprojectapp'

    def __str__(self):
        return self.name