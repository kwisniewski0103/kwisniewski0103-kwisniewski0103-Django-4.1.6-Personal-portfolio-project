from django.db import models



class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=False, null=True)

    def __str__(self):
        return self.title




