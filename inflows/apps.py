from django.apps import AppConfig


class InflowsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inflows'

    def ready(self): #estamos sobrescrevendo o método e com isso ativamos o signals para "ouvir" as entradas
        import inflows.signals 