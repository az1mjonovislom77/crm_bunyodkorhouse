from django.contrib import admin
from home.models import Home, FloorPlan


@admin.register(FloorPlan)
class FloorPlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'home']


class FloorPlanInline(admin.TabularInline):
    model = FloorPlan
    extra = 1


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['id', 'home_number', 'floor']
    list_filter = ('home_number', 'floor', 'blocks', 'rooms')
    search_fields = ('home_number', 'blocks', 'rooms', 'floor', 'area')
    inlines = [FloorPlanInline]
