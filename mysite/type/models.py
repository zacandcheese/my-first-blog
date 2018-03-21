from django.db import models

class Info(models.Model):
    author = models.CharField()
    charLib = models.TextField()
    timeLib = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.author