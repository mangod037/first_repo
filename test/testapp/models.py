from django.db import models
from django.conf import settings
from DBtest.utils import uniqueSlugGenerator
from django.db.models.signals import pre_save
from django.shortcuts import reverse

# Create your models here.
class AllServices(models.Model):
    engName = models.CharField(max_length=50)
    company = models.CharField(max_length=30)
    price = models.FloatField()
    slug = models.SlugField(unique=True, max_length=150)
    # siteLink = models.URLField()

    def __str__(self):
        return self.engName

# slug 생성/저장
def slugSave(sender, instance, *args, **kargs):
    if not instance.slug:
        instance.slug = uniqueSlugGenerator(instance, instance.engName, instance.slug)
pre_save.connect(slugSave, sender=AllServices)


class SelectedService(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    service = models.ForeignKey(AllServices, on_delete=models.CASCADE)
    selected = models.BooleanField(default=False)

    def __str__(self):
        return self.service.slug

class Select(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    services = models.ManyToManyField(SelectedService)
    # startDate = models.DateTimeField(auto_now_add=True)
    selected = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username