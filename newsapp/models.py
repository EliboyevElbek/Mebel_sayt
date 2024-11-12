from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=50, verbose_name='Mebel turini kiriting')


    def __str__(self):
        return self.cat_name

    class Meta:
        verbose_name_plural = 'Categories'

class Mebel(models.Model):
    title = models.CharField(max_length=350, verbose_name='Mebel nomi')
    summary = models.CharField(max_length=450, blank=True, null=True, verbose_name='Mebel haqida qisqacha ta\'rif')
    body = RichTextField(verbose_name='Mebel haqida batafsil ma\'lumot')
    categoty = models.ForeignKey(Category, default=1, on_delete=models.CASCADE, verbose_name='Mebel turini tanlang')
    image = models.ImageField(upload_to='image/', blank=True, null=True, verbose_name='Mebel rasmi')
    material = models.CharField(max_length=200, blank=True, null=True, verbose_name='Mebelda ishlatilgan material')
    price = models.CharField(max_length=50, verbose_name='Mebelni sotilish narxi')
    rek_price = models.CharField(max_length=50, blank=True, null=True, verbose_name='Mebel reklama narxi')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_product', args=[str(self.pk)])

