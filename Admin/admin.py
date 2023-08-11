from django.contrib import admin
from .models import Block,Block_Location,Room,Role,User
# Register your models here.
admin.site.register(Block)
admin.site.register(Block_Location)
admin.site.register(Room)
admin.site.register(Role)
admin.site.register(User)