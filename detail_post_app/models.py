from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Detail(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True, null=True)
    img = models.ImageField()
    created = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    slug = models.SlugField(blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title


class Main(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True, null=True)
    img = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title
