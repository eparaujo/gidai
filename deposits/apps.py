from django.apps import AppConfig


class DepositsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'deposits'

    def ready(self): #estamos sobrescrevendo o método e com isso ativamos o signals para "ouvir" as entradas
        import deposits.signals 
