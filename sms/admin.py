from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from leaflet.forms.widgets import LeafletWidget

from MpWsn.settings import LEAFLET_WIDGET_ATTRS
from sms.models import LocationSoilSensorData

# Register your models here.

admin.site.register(LocationSoilSensorData, LeafletGeoAdmin)

LEAFLET_FIELD_OPTIONS = {'widget': LeafletWidget(attrs=LEAFLET_WIDGET_ATTRS)}

