from rest_framework.serializers import ModelSerializer, ReadOnlyField
from . import models


# class ActividadSerializer(Serializer):
#     month = CharField()
#     count = IntegerField()
class PresentacionSerializer(ModelSerializer):

    class Meta:
        model = models.Presentacion
        fields = '__all__'


class ActividadSerializer(ModelSerializer):
    category = ReadOnlyField(source='category.category.title')
    color = ReadOnlyField(source='category.category.color')
    salon = ReadOnlyField(source='salon.title')

    presentaciones = PresentacionSerializer(many=True)

    class Meta:
        model = models.Actividad
        fields = '__all__'


class ActivityCategorySerializer(ModelSerializer):
    actividades = ActividadSerializer(many=True)

    class Meta:
        model = models.ActivityCategory
        fields = '__all__'


class CategoryNestedItemSerializer(ModelSerializer):

    activity_category = ActivityCategorySerializer(many=True)

    class Meta:
        model = models.CategoryItem
        fields = '__all__'


class CategoryItemSerializer(ModelSerializer):
    class Meta:
        model = models.CategoryItem
        fields = '__all__'


class SponsorSerializer(ModelSerializer):
    class Meta:
        model = models.Sponsor
        fields = '__all__'


class AsistenteSerializer(ModelSerializer):
    class Meta:
        model = models.Asistente
        fields = '__all__'


class ProfesorSerializer(ModelSerializer):
    class Meta:
        model = models.Profesor
        fields = '__all__'


class ProfesorCategorySerializer(ModelSerializer):
    profesores = ProfesorSerializer(many=True)

    class Meta:
        model = models.ProfesorCategory
        fields = '__all__'


class AnuncioSerializer(ModelSerializer):
    class Meta:
        model = models.Anuncio
        fields = '__all__'
