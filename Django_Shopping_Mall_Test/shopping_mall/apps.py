from django.apps import AppConfig


class ShoppingMallConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shopping_mall'

    def ready(self):
        import shopping_mall.signals