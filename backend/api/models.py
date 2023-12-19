# MODELS

from django.db import models

class File(models.Model):
    pdf = models.FileField(upload_to='store/pdfs/')

    def __str__(self):
        return str(self.pdf)
