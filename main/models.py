from django.db import models



class About(models.Model):
    image = models.ImageField(upload_to='images/')
    text = models.TextField()
    about_text = models.TextField()
    def __str__(self):
        return self.text

class Specialized(models.Model):
    name = models.CharField(max_length=50)
    nomer = models.IntegerField()
    def __str__(self):
        return self.name

class Categoriya(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Portfolio(models.Model):
    categoriya = models.ForeignKey(Categoriya, null=True, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Experience(models.Model):
    name = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    text = models.TextField()
    def __str__(self):
        return self.name


class Team(models.Model):
    img = models.ImageField(upload_to='images/')
    job = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    text = models.TextField()
    def __str__(self):
        return self.name


class News(models.Model):
    img = models.ImageField(upload_to='images/')
    name = models.TextField()
    text = models.TextField()
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.name

