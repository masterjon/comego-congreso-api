from rest_framework.viewsets import ModelViewSet
# from rest_framework.generics import ListAPIView
# from django.db.models import Count

from . import serializers, models


# class ActivityDatesViewSet(ListAPIView):
#     serializer_class = serializers.ActividadSerializer

#     def get_queryset(self):
#         return models.Actividad.objects.values("month").annotate(count=Count("month"))
class ActivityViewSet(ModelViewSet):
    queryset = models.Actividad.objects.all()
    serializer_class = serializers.ActividadSerializer


class CategoryItemViewSet(ModelViewSet):
    queryset = models.CategoryItem.objects.all()
    serializer_class = serializers.CategoryItemSerializer


class CategoryNestedItemViewSet(ModelViewSet):
    queryset = models.CategoryItem.objects.all()
    serializer_class = serializers.CategoryNestedItemSerializer


class SponsorViewSet(ModelViewSet):
    queryset = models.Sponsor.objects.all()
    serializer_class = serializers.SponsorSerializer


class AsistenteViewSet(ModelViewSet):
    queryset = models.Asistente.objects.all()
    serializer_class = serializers.AsistenteSerializer


class ProfesorCategoryViewSet(ModelViewSet):
    queryset = models.ProfesorCategory.objects.all()
    serializer_class = serializers.ProfesorCategorySerializer
