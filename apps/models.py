from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="images", blank=True)

    def __str__(self):
        return self.title
