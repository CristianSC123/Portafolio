from django.db import models
from apps.Analisis.views import generar_embedding
import uuid

class Informacion(models.Model):
    idInformation = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fullName = models.CharField(max_length=35)
    specialty = models.CharField(max_length=40)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    urlWeb=models.URLField(max_length=200)
    embedding=models.JSONField(null=True, blank=True)
    
    class Meta:
        db_table = 'Informacion'
        verbose_name = 'Informacion'
        verbose_name_plural = 'Informaciones'
        
    def save(self, *args, **kwargs):
        if(self.fullName and self.email and self.phone and self.specialty):
            texto = (
                f"fullName: {self.fullName}, "
                f"email: {self.email}, "
                f"phone: {self.phone}, "
                f"specialty: {self.specialty}"
            )
            self.embedding = generar_embedding(texto)
        super(Informacion, self).save(*args, **kwargs)
            
    def __str__(self):
        return f'{self.fullName}'
 
class SocialMedia(models.Model):
    idSocialMedia = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idInformation = models.ForeignKey(Informacion, on_delete=models.CASCADE)
    name = models.CharField(max_length=35)
    url = models.URLField(max_length=200)
    embedding = models.JSONField(null=True, blank=True)   
    
    class Meta:
        db_table = 'SocialMedia'
        verbose_name = 'SocialMedia'
        verbose_name_plural = 'SocialMedias'