from django.db import models


class Email(models.Model):
    address = models.EmailField(null=True)

    def __str__(self):
        return self.address


class Message(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    email_from = models.EmailField(null=True)
    subject = models.CharField(blank=True, max_length=500)
    date = models.DateTimeField(null=True)
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    body = models.CharField(blank=True, max_length=5000)
    attachment = models.CharField(blank=True, max_length=1000)

    def __str__(self):
        return self.email_from
