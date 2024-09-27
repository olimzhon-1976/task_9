from django.db import models


class Prediction(models.Model):
    text = models.TextField()


class Poem(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    theme = models.CharField(max_length=50)
    text = models.TextField()

    class Meta:
        db_table = "poem"

    def __str__(self):
        return self.title