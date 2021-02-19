from django.db import models
from django.conf import settings
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel


class Location(BaseModel):

    address = models.CharField('Direccion', max_length=100, unique = False, blank = False, null = True)
    city = models.CharField('Ciudad', max_length=100, unique = False, blank = False, null = False)
    state_name = models.CharField('Estado', max_length=100, unique = False, blank = False, null = False)
    x_coord = models.FloatField()
    y_coord = models.FloatField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    historical = HistoricalRecords

    # Redondea numeros reales a partir de 6 decimales.
    def save(self, *args, **kwargs):
        self.x_coord = round(self.x_coord, 6)
        self.y_coord = round(self.y_coord, 6)
        super(Location, self).save(*args, **kwargs)

    class Meta:

        verbose_name = 'Localización'
        verbose_name_plural = 'Localizaciónes'

    def __str__(self):
        return f'Coordenadas: {str(self.x_coord)} : {str(self.y_coord)}'


class Pay(BaseModel):

    quantity = models.FloatField()
    cryptocurrency = models.CharField('Criptodivisa', max_length=50, blank = False, unique = False, null = False)
    location = models.OneToOneField('Location', on_delete=models.CASCADE)
    wallet_address = models.CharField('Wallet', max_length= 32, blank = False, unique = False, null = False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    historical = HistoricalRecords

    def save(self, *args, **kwargs):
        self.quantity = round(self.quantity, 7)
        super(Pay, self).save(*args, **kwargs)

    class Meta:

        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'

    def __str__(self):
        return 'pay_' + str(self.id)