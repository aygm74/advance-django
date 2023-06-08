from django.db import models 



class Comments(models.Model):
    title=models.CharField(max_length=120,verbose_name="نام")
    email=models.EmailField(max_length=300,verbose_name="ایمیل")
    status=models.BooleanField(default=True)
    description=models.TextField(blank=True)

    def get_snippet(self):
        return self.description[0:20] 


class Category(models.Model):
    name=models.CharField(max_length=120,verbose_name='دسته بندی')
    
 