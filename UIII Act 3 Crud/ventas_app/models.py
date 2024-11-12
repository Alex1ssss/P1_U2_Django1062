from django.db import models

# Create your models here.

class Ventas(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    id_cliente = models.CharField(max_length=6)
    total_venta=models.DecimalField(decimal_places=2, max_digits=2)
    metodo_pago=models.CharField(max_length=20)
    id_empleado= models.CharField(max_length=6)

    def __str__(self):
        return self.codigo