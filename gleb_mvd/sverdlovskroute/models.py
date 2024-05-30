from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Interesting_place(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.TextField()
    img = models.ImageField(upload_to='images/', blank=True, null=True)
    favourites = models.ManyToManyField(User, related_name='favourites', blank=True)
    

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Weekend_rout(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    interesting_place = models.ManyToManyField(Interesting_place)
    location = models.TextField()
    img = models.ImageField(upload_to='images/', blank=True, null=True)
    favourites_routes = models.ManyToManyField(User, related_name='favourites_routes', blank=True)
    

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
    

class Favorite_rout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    route = models.ForeignKey(Weekend_rout, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'route')


class Favorite_place(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interesting_place = models.ForeignKey(Interesting_place, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'interesting_place')

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000)
    antwort = models.TextField(max_length=1000, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # Будет отображаться следующее поле в панели администрирования
        return self.email + '*' + self.antwort 
    

class Answer(models.Model):
    text = models.TextField(max_length=1000)
    relation_contact = models.ForeignKey(Contact, on_delete=models.CASCADE)