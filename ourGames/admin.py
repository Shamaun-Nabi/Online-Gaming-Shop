from django.contrib import admin
from .models import Game,Category

# Register your models here.
class gameTable(admin.ModelAdmin):
    list_display=['name','price','category','publisher']


admin.site.register(Game,gameTable)
admin.site.register(Category)

