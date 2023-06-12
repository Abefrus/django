from django.db import models
from django.shortcuts import render
from .models import MyModel

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    # Додайте інші поля за потреби

    def __str__(self):
        return self.name
    
    def my_data_view(request):
        data = MyModel.objects.all()
        return render(request, 'my_data_template.html', {'data': data})
        