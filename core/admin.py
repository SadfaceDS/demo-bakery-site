from django.contrib import admin
from core.models import *
from django.forms import ModelForm


# Register your models here.


class menuAdmin(admin.ModelAdmin):
    list_display = ('food_type', 'picture', 'item_name', 'item_description', 'item_price')
    search_fields = ('food_type', 'item_name')
    ordering = ('item_name', )
    fieldsets = (
        ('Item', {'fields': ('food_type', 'item_name', 'item_description')}),
        ('Stats', {'fields': ('picture', 'item_price')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'item_name', 'item_description', 'food_type', 'picture_link', 'item_price'),
        }),
    )


class testAdmin(admin.ModelAdmin):
    list_display = ('message', 'name')
    search_fields = ('name',)
    ordering = ('name', )
    fieldsets = (
        ('Items', {'fields': ('name', 'message')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'name', 'message'),
        }),
    )


class HomeStarTreatForm(ModelForm):
    def clean(self):
        # If this is a *new* object (no PK yet)
        if not self.instance.pk and homeStarTreat.objects.count() >= 3:
            raise ValidationError("You can only have up to 3 Star Treats.")
        return super().clean()


class homeStarTreatsAdmin(admin.ModelAdmin):
    form = HomeStarTreatForm
    list_display = ('message', 'name')
    search_fields = ('name',)
    ordering = ('name',)
    fieldsets = (
        ('Items', {'fields': ('name', 'message')}),
    )


class MemberMessagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'message')
    search_fields = ('name', 'email', 'message', 'date')
    ordering = ('-date',)

admin.site.register(MenuItem, menuAdmin)
admin.site.register(Testimonial, testAdmin)
admin.site.register(homeStarTreat, homeStarTreatsAdmin)
admin.site.register(memberMessages, MemberMessagesAdmin)

