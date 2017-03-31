from django.db import models

class Familia(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Subtipo(models.Model):
    nombre = models.CharField(max_length=100)
    familia_ID = models.ForeignKey(Familia,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Acabado(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Material(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class TipoMedida(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    descripcion=models.CharField(max_length=500)
    medida1=models.FloatField()
    medida2=models.FloatField()
    familia_ID=models.ForeignKey(Familia,on_delete=models.CASCADE)
    subtipo_ID=models.ForeignKey(Subtipo,on_delete=models.CASCADE)
    acabado_ID=models.ForeignKey(Acabado,on_delete=models.CASCADE)
    material_ID=models.ForeignKey(Material,on_delete=models.CASCADE)
    tipoMedida_ID=models.ForeignKey(TipoMedida,on_delete=models.CASCADE)
    def __str__(self):
        return self.descripcion