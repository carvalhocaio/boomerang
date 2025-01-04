from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.urls import path

urlpatterns = [
    path('', admin.site.urls),
]

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.site_header = 'Boomerang Admin'
admin.site.site_title = 'Boomerang Admin Portal'
admin.site.index_title = 'Welcome to Boomerang Portal'
