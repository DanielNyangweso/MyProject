from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField  # type: ignore # Assuming you're using CKEditor for RichTextField

class Product(models.Model):
    # Fields for the Product model
    name = models.CharField(max_length=255)  # Added name field (needed for slug generation)
    price = models.FloatField(default=0.0)  # `max_length` is not applicable to FloatField
    image = models.ImageField(null=True, blank=True, upload_to="products/")
    description = RichTextField(null=True, blank=True)  # Using CKEditor's RichTextField
    slug = models.SlugField(unique=True, null=True, max_length=400)  # Fixed SlugField syntax
    created_at = models.DateTimeField(auto_now_add=True)  # Fixed capitalization

    def get_absolute_url(self):
        # Returns the URL for the product detail page
        return reverse('product_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    def save(self, *args, **kwargs):
        # Automatically generates a slug if not provided
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        # String representation of the Product object
        return f'{self.name} - {self.created_at}'
