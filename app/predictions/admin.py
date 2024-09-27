from django.contrib import admin
from .models import Prediction, Poem


admin.site.register(Prediction)
admin.site.register(Poem)