from django.apps import AppConfig


class WithdrawalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'withdrawals'

    def ready(self): #estamos sobrescrevendo o método e com isso ativamos o signals para "ouvir" as entradas
        import withdrawals.signals 
