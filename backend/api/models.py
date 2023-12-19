# MODELS

from django.db import models

class Files(models.Model):
    pdf = models.FileField(upload_to='store/pdfs/')

    def __str__(self):
        return self.pdfs
