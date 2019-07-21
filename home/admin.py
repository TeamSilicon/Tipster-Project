from django.contrib import admin
from .models import Match, Market, Outcome

# Register your models here.

admin.site.register(Match)
admin.site.register(Market)
admin.site.register(Outcome)
