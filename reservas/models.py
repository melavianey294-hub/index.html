from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    habitacion = models.CharField(max_length=10)

    def __str__(self):
        return f"Reserva de {self.cliente.nombre} del {self.fecha_entrada} al {self.fecha_salida}"
