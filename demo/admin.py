from django.contrib import admin
from songsrank import models
from . import models as demo_model

# Register your models here.
admin.site.register(models.New_Song_Rank)
admin.site.register(models.Hot_Song_Rank)
admin.site.register(models.Douyin_Song_Rank)
admin.site.register(models.Popular_Song_Rank)
admin.site.register(demo_model.Songs)
admin.site.register(demo_model.Albums)
admin.site.register(demo_model.Singers)
