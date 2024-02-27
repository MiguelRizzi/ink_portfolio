from django.contrib import admin
from .models import Tattoo, Design, Message

admin.site.register(Tattoo)
admin.site.register(Design)
admin.site.register(Message)