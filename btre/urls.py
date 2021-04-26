#  This contains python scripts that will store all the url patterns for the project. Basically the different pages of your application

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
