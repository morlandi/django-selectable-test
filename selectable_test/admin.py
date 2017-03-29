# -*- coding: UTF-8 -*-
from django.contrib import admin
from .models import Country
from .models import City
from .models import Machine
from .forms import MachineAdminForm
from .utils import trace

####################################################################################################
# Data models

class BaseModelAdmin(admin.ModelAdmin):
    """
    Base class for 'shared' model admins;
    manages common metadata
    """
    search_fields = ['=id', 'description']
    list_display = ['__str__', 'id', ]


class CityInline(admin.TabularInline):
    readonly_fields = ['id', ]
    fields = ['description', ]
    extra = 0
    model = City


@admin.register(Country)
class CountryAdmin(BaseModelAdmin):
    inlines = [CityInline, ]


@admin.register(City)
class CityAdmin(BaseModelAdmin):
    list_display = ['__str__', 'country', 'id']
    list_filter = ['country', ]


@admin.register(Machine)
class MachineAdmin(BaseModelAdmin):
    form = MachineAdminForm
    list_display = ['__str__', 'country', 'city', 'id']
    list_filter = ['country', 'city', ]

    class Media:
        js = (
            "admin/js/machine_admin.js",
        )

    def change_view(self, request, object_id, form_url='', extra_context=None):
        trace(request.POST)
        return super(MachineAdmin, self).change_view(request, object_id, form_url, extra_context)
