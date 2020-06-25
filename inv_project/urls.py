from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('invapp.urls')),
    path('admin/', admin.site.urls),

    # path('accounts/', include('registration.backends.default.urls')),
]
