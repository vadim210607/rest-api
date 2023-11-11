"""
URL configuration for config project.

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
from django.urls import path, include
from rest_framework import routers

from catalog.views import PerfumViewSet, BottleView, UserListAPI

# router = routers.SimpleRouter()
router = routers.DefaultRouter()
router.register(r'perfum', PerfumViewSet, basename='perfum')
router.register(r'bottle', BottleView, basename='bottle')
router.register(r'user', UserListAPI)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
print(router.urls)

# На основі ViewSet
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/perfumlist/', PerfumViewSet.as_view({'get': 'list'})),
#     path('api/v1/perfumlist/<int:pk>/', PerfumViewSet.as_view({'put': 'update'})),
# ]

# На основі Generic Class Based
# from catalog.views import PerfumAPIList, PerfumAPIUpdate, PerfumAPIGRUD
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/perfumlist/', PerfumAPIList.as_view()),
#     path('api/v1/perfumlist/<int:pk>/', PerfumAPIUpdate.as_view()),
#     path('api/v1/perfumdetail/<int:pk>/', PerfumAPIGRUD.as_view())
# ]
