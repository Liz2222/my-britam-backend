from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Users)
admin.site.register(Policy)
admin.site.register(PolicyTypes)
admin.site.register(UserPolicy)
admin.site.register(Profile)
admin.site.register(Transaction)
admin.site.register(LoyaltyPoints)
admin.site.register(EducationContent)