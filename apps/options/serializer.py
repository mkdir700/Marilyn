from rest_framework import serializers
from .models import OptionsModel


class OptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = OptionsModel
        fields = '__all__'
