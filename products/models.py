from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    stripe_product_id = models.CharField(max_length=100)
    file = models.FileField(upload_to="product_files/", blank=True, null=True)
    url = models.URLField()

    def __str__(self):
        return self.name


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0)  # cents

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
