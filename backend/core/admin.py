from django.contrib import admin

# Register your models here.

admin.site.site_header = 'Farmcare Admin'
admin.site.site_title = 'Farmcare Admin Portal'

admin.autodiscover()

class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ('added_at', 'added_by', 'updated_at', 'updated_by')