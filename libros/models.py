from django.db import models

class Libro(models.Model):
    autor = models.CharField(max_length=30)
    titulo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    editorial = models.CharField(max_length=30)
    fecha_publicacion = models.DateField()
    portada = models.ImageField(upload_to="portadas/", null= "true", blank = "true" )
    
    def __str__(self) -> str:
        return f"{self.titulo} - {self.autor} - {self.precio}$"