from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=120, verbose_name='دسته بندی')


class Comments(models.Model):
    title = models.CharField(max_length=120, verbose_name="نام")
    email = models.EmailField(max_length=300, verbose_name="ایمیل")
    status = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def get_snippet(self):
        return self.description[0:20]

    def get_absolute_api_url(self):
        return reverse("api-v1:post-detail", kwargs={"pk": self.pk})
