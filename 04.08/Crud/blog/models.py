from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    review = models.TextField()
    price = models.FloatField()

    one = '★'
    two = '★★'
    three = '★★★'
    four = '★★★★'
    five = '★★★★★'
    score_choices = (
        (one, '★'),
        (two, '★★'),
        (three, '★★★'),
        (four, '★★★★'),
        (five, '★★★★★')
    )
    starScore = models.CharField(
        max_length = 5,
        choices = score_choices,
        default = one
        )


    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()



# class ScoreChoice(models.Model):
#     one = '1'
#     two = '2'
#     three = '3'
#     four = '4'
#     five = '5'
#     score_choices = (
#         (one, '★'),
#         (two, '★★'),
#         (three, '★★★'),
#         (four, '★★★★'),
#         (five, '★★★★★'),
#     )
#     starScore = models.CharField(
#         max_length=2,
#         choices = score_choices,
#         default = one,
#         )

#     def is_upperclass(self):
#         return self.starScore in (self.one, self.five)
