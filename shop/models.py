from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shop', null=True)

class Comment(models.Model):
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

#https://stackoverflow.com/questions/74706092/django-imagefield-with-multiple-images
class ItemAttachment(models.Model):
    file = models.ImageField("Attachment", upload_to='shop/')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='item')

    class Meta:
        verbose_name = 'Item Attachment'
        verbose_name_plural = 'Item Attachments'

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'category']

    item_attachment = forms.ImageField()




