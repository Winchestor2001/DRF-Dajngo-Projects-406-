from django.db import models


class Jora(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='jora_img/')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.description}"
