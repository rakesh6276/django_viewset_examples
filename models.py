from django.db import models

class Paradigm(models.Model):
    name = models.CharField(max_length=50)


class language(models.Model):
    name = models.CharField(max_length=50)
    paradigm = models.ForeignKey(Paradigm, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=50)
    language = models.ManyToManyField(language)

    def __str__(self):
        return self.name
