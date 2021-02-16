from django.apps import AppConfig


class BaseConfig(AppConfig):
    name = 'base'
    
class PaymentsConfig(AppConfig):
    name = 'payments'
