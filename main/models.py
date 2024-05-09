from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField('Name', max_length=50)
    task = models.TextField('Description' )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = "Задачи"


# class Mesk(models.Model):
#     predmet = models.CharField('Predmet:', max_length=30)
#     numberClass = models.IntegerField("Class: ")
#
#     def __str__(self):
#         return self.predmet
#