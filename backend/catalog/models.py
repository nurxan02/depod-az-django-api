from django.db import models


class Category(models.Model):
    key = models.SlugField(max_length=50, unique=True, help_text='Identifier used in frontend (e.g., earphone)')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    id = models.SlugField(primary_key=True, max_length=100, help_text='Slug ID matching frontend, e.g., peak-black')
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    description = models.TextField(blank=True)
    # prices optional; keep nullable since current frontend hides price
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    is_main = models.BooleanField(default=False)
    alt = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']


class ProductFeature(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='features')
    text = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']


class ProductSpec(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specs')
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']


class ProductHighlight(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='highlights')
    number = models.CharField(max_length=50)
    text = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']
