from django.db import models
from django.urls import reverse


class Categories(models.Model):
    title = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Notes(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    reminder = models.CharField(max_length=255)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('edit_note', args=[str(self.id)])

    class Meta:
        verbose_name_plural = 'Notes'

    def __str__(self):
        return f'{self.title} {self.text} {self.reminder}'

