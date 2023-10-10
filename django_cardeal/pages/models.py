from django.db import models


class Teams(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation=models.CharField(max_length=255)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link=models.URLField(max_length=200)
    instagram_link=models.URLField(max_length=200)
    x_link=models.URLField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

class ContactMsg(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"




