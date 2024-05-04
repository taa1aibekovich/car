from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.category_name


class Marka(models.Model):
    marka_name = models.CharField(max_length=16, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.marka_name


class Model(models.Model):
    model_name = models.CharField(max_length=16, unique=True)
    marka = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name


class Car(models.Model):
    name_car = models.CharField(max_length=32)
    price = models.PositiveIntegerField(default=0)
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CharField)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    year = models.SmallIntegerField(default=2024)
    type = models.BooleanField(default=False)
    image = models.ImageField(upload_to='img')
    volume = models.FloatField(default=0.8)

    def __str__(self):
        return self.name_car
