"""
URL configuration for khoeletso project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from core.viewsets import *
from core import views
router = routers.DefaultRouter()
router.register(r'product', ProductViewset)
router.register(r'product-create', ProductCreateViewset)
router.register(r'farmers', FarmerViewSet)

from django.conf.urls.static import static  # new
from django.conf import settings  # new

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_authtoken.urls')),
    path('login/', views.custom_login, name='custom_login'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
# urlpatterns +=router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #new

