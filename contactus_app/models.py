from django.db import models


class Text(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title


class Contactus (models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True , blank=True)
    subject = models.CharField(max_length=100)
    text = models.TextField(null=True , blank=True)
    created = models.DateTimeField(blank=True,null=True,auto_now_add=True)

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
