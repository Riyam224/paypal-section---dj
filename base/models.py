from django.db import models
from django.db.models.base import Model

# Create your models here.
from django.utils.translation import ugettext_lazy as _

class Product(models.Model):
    name = models.CharField(_("name"), max_length=50)
    description = models.TextField(_("description"))
    image_url = models.ImageField(_("image"), upload_to='images' , blank=True , null=True)
    price = models.FloatField(blank=True , null=True)
    

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, blank=True , null=True , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return self.product.name

  