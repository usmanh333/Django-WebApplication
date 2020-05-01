from django.contrib import admin
from .models import PostServices,Category,Location,Area


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


# class PostServicesAdmin(admin.ModelAdmin):
#     list_display = ('author', 'date_posted', 'category_posted')
# PostServicesAdmin

admin.site.register(PostServices)
admin.site.register(Location)
admin.site.register(Area)