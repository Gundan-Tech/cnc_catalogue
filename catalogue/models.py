from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    # 2. Product Name
    name = models.CharField(max_length=200)
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    # 1. Product Images (4 maximum)
    image_1 = models.ImageField(upload_to='products/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='products/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='products/', blank=True, null=True)
    image_4 = models.ImageField(upload_to='products/', blank=True, null=True)

    # 3. Size details (using Float for decimals like 10.5)
    length = models.FloatField(help_text="Length in cm or inches")
    width = models.FloatField(help_text="Width in cm or inches")
    thickness = models.FloatField(help_text="Thickness in cm or inches")

    # 4. Price
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # 5. Minimum Order
    minimum_order = models.IntegerField(default=1)

    # 6. Delivery details and other info
    delivery_time = models.CharField(max_length=100, help_text="e.g., 7-14 business days")
    description = models.TextField(blank=True, null=True, help_text="Any other important details")

    # This makes the product show up by its name in the admin panel
    def __str__(self):
        return self.name