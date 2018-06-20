from django.contrib import admin
from . import models
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class AsistenteResource(resources.ModelResource):
    class Meta:
        model = models.Asistente


class ProfesorResource(resources.ModelResource):
    class Meta:
        model = models.Profesor


@admin.register(models.CategoryItem)
class CategoryItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ActivityCategory)
class ActivityCategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "ordering"]
    list_filter = ["category"]


@admin.register(models.Salon)
class SalonAdmin(admin.ModelAdmin):
    pass


class PresentacionTabAdmin(admin.StackedInline):
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
class ProfesorAdmin(ImportExportModelAdmin):
    list_display = ["nombres", "category"]
    list_filter = ["category"]
    resource_class = ProfesorResource


@admin.register(models.Asistente)
class AsistenteAdmin(ImportExportModelAdmin):
    resource_class = AsistenteResource
    search_field = ["nombre"]
