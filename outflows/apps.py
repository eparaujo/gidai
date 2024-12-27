from django.apps import AppConfig


class OutflowsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'outflows'
    
    def ready(self): #estamos sobrescrevendo o método e com isso ativamos o signals para "ouvir" as entradas
        import outflows.signals 