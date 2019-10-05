from django.utils.translation import ugettext_lazy as _

from django_filters import rest_framework as filters

from .models import Property


class PropertyFilter(filters.FilterSet):
    class Meta:
        model = Property
        fields = {
            'price': ['lt', 'gt'],
            'rooms': ['exact'],
            'guests': ['exact'],
            'neighborhood': ['iexact'],
        }
