from django.db import models


class DatasetModels(models.Model):
    file = models.FileField()
    serialized_model = models.TextField()