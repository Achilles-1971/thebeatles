from django.db import models

class Participant(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='participants/', null=True, blank=True)

    def __str__(self):
        return self.name
