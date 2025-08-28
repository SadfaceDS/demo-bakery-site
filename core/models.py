from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.


class MenuItem(models.Model):
    id = models.AutoField(primary_key=True)
    food_type = models.CharField(max_length=20, null=False, blank=False)
    picture = models.ImageField(upload_to='menu_images/', null=True, blank=True)
    item_name = models.CharField(max_length=40, null=False, blank=False)
    item_description = models.CharField(max_length=100, null=False, blank=False)
    item_price = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)

    class Meta:
        db_table = 'menu_items'

    def __str__(self):
        return self.item_name


class Testimonial(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        db_table = 'testimonials'

    def __str__(self):
        return self.name


class homeStarTreat(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        db_table = 'star treats'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk and homeStarTreat.objects.count() >= 3:
            raise ValidationError("You can only have up to 3 Star Treats.")
        super().save(*args, **kwargs)



class memberMessages(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=500, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'member_messages'

    def __str__(self):
        return f"{self.name} - {self.date}"