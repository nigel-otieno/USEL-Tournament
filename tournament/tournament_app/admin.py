from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Tournament)
admin.site.register(Team)
admin.site.register(Players)
admin.site.register(TimeBasedGameMode)
admin.site.register(ScoreBasedGameMode)
admin.site.register(HybridGameMode)
admin.site.register(Bracket)
