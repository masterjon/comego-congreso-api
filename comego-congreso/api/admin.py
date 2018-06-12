from django.contrib import admin
from . import models


@admin.register(models.CategoryItem)
class CategoryItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ActivityCategory)
class ActivityCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Salon)
class SalonAdmin(admin.ModelAdmin):
    pass


class PresentacionTabAdmin(admin.TabularInline):
    model = models.Presentacion


@admin.register(models.Actividad)
class ActividadAdmin(admin.ModelAdmin):
    readonly_fields = ('month',)
    list_display = ["title", "category", "start_date", "ordering"]
    list_filter = ["category"]
    inlines = [PresentacionTabAdmin]


@admin.register(models.Presentacion)
class PresentacionAdmin(admin.ModelAdmin):
    list_display = ["title", "actividad"]
    list_filter = ["actividad"]


@admin.register(models.Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ProfesorCategory)
class ProfesorCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Asistente)
class AsistenteAdmin(admin.ModelAdmin):
    pass
