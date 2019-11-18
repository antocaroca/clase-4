from django.db import models

class ActiveManager(models.Model):
    def active(self):
        return self.filter(active=True)


class Producto(models.Model):
    name = models.CharField(max_length=32, help_text='Nombre del producto')
    description = models.TextField(blank=True,  help_text='Descripción del producto')
    price = models.DecimalField(max_digits=6, decimal_places=2,  help_text='precio del producto')
    active = models.BooleanField(default=True, help_text='Producto activo')
    date_update = models.DateTimeField(auto_now=True, help_text='Fecha de actualización del producto')

    objects = ActiveManager()

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Products'
        ordering = ('pk',)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Producto, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product-images")

class ProducTag(models.Model):
    products = models.ManyToManyField(Producto, blank=True)
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=48)
    description = models.TextField(blank=True, null="")
    active = models.BooleanField(default=True)
