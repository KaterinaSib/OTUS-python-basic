from django.contrib import admin
from django.urls import path, include
from meters.views import index_list_view

urlpatterns = [
    path("", index_list_view, name="index"),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("addresses/", include("addresses.urls")),
    path("meters/", include("meters.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
]
