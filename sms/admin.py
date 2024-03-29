from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from leaflet.forms.widgets import LeafletWidget

from MpWsn.settings import LEAFLET_WIDGET_ATTRS
from sms.models import SensorGroup, SensorCollectedData

# Register your models here.

admin.site.register(SensorGroup, LeafletGeoAdmin)
admin.site.register(SensorCollectedData, LeafletGeoAdmin)

LEAFLET_FIELD_OPTIONS = {'widget': LeafletWidget(attrs=LEAFLET_WIDGET_ATTRS)}


