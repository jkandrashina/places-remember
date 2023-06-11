from django.contrib import admin
from .models import PlaceRemember
from treasuremap import widgets


@admin.register(PlaceRemember)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('place_name', 'author', 'pub_date')

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'location':
            kwargs['widget'] = widgets.AdminMapWidget()
        return super(PlaceAdmin, self).formfield_for_dbfield(db_field, **kwargs)
