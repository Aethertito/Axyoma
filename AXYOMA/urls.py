
''' URL configuration for AXYOMA project.
    The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/

    - Function views
        1. Add an import:  from my_app import views
        2. Add a URL to urlpatterns:  path('', views.home, name='home')
    - Class-based views
        1. Add an import:  from other_app.views import Home
        2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
    - Including another URLconf
        1. Import the include() function: from django.urls import include, path
        2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
'''

# ---------------------------------------------------------------------------- #

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # URLs del panel de administración de DJANGO.

    path('api/', include('api.urls')), # URLs de la API.
    path('axyoma/', include('surveys.urls')), # URLs de las encuestas.
    path('management/', include('dashboard.urls')), # URLs del Dashboard.
    path('', include('public.urls')), # URLs de acceso público.
]

# ---------------------------------------------------------------------------- #
# from django.conf import settings
# from django.conf.urls.static import static
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# ---------------------------------------------------------------------------- #

# SURVEYS_URLS


# ---------------------------------------------------------------------------- #