from django.db import models

class About(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_de_registro = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} - {self.email}"
