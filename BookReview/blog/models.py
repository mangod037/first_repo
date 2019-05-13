from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    review = models.TextField(null=True)
    price = models.FloatField(null=True, default=None)

    one='★'
    two='★★'
    three='★★★'
    four='★★★★'
    five='★★★★★'
    scoreChoice = (
        (one, '★'),
        (two, '★★'),
        (three, '★★★'),
        (four, '★★★★'),
        (five, '★★★★★')
    )
    starScore = models.CharField(max_length=10, choices=scoreChoice, default=one)

    image = models.FileField(null=True)
    author = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField(null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=30, default='')