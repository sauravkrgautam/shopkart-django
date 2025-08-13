from django.contrib import admin

from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug', 'short_description', 'cat_image')
    list_display_links = ('category_name', 'short_description')
    prepopulated_fields = {'slug': ('category_name',)}
    search_fields = ('category_name', 'slug')
    list_filter = ('category_name',)

    def short_description(self, obj):
        return obj.description[:50] if obj.description else 'No description'

admin.site.register(Category, CategoryAdmin)


admin.site.site_header = "ShopKart Admin"
admin.site.site_title = "ShopKart Admin Portal"

admin.site.index_title = "Welcome to ShopKart Admin Portal"

admin.site.site_url = None  # Disable the link to the admin site from the header
admin.site.enable_nav_sidebar = False  # Disable the sidebar navigation
admin.site.empty_value_display = 'N/A'  # Display 'N/A' for empty fields in the admin interface
admin.site.default_permissions = ()  # Disable default permissions for the admin site
admin.site.has_permission = lambda request: request.user.is_authenticated  # Ensure only authenticated users can access the admin site
admin.site.login_template = 'admin/login.html'  # Custom login template for the admin site
admin.site.logout_template = 'admin/logout.html'  # Custom logout template for the admin site''

