from django.db import models

class SiteStatus(models.Model):
    status = models.BooleanField(default=True)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return str(self.status)