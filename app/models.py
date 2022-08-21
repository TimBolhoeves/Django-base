from django.db import models
from django.urls import reverse
import django.utils.timezone

# Create your models here.

# class YourModel(models.Model):
#     company = models.CharField(max_length=255, default='none')
#     subject = models.CharField(max_length=255, default='none')
#     category = models.CharField(max_length=255, default='Other')
#     question = models.TextField(default='none')
#     answer = models.CharField(max_length=255, default='none')
#     date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.company

#     def get_absolute_url(self):
#         return reverse("yourmodel_detail", kwargs={"pk": self.pk})