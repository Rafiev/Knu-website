from django.db import models

class Сompound(models.Model):
    
    class Position(models.TextChoices):
        DIRECTOR = 'Директор'
        TEACHER = 'Преподаватель'
        MANAGER = 'Менеджер'

    name = models.CharField(max_length=30, null=True)
    position = models.CharField(max_length=20, choices=Position.choices, default=Position.TEACHER,)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self) -> str:
        return self.name    


class News(models.Model):
    created_at = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=30, null=True)
    description = models.TextField(null=True)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self) -> str:
        return self.title


class Image(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')

