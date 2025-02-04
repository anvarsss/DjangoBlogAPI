from django.contrib import admin
from django.urls import path, include , re_path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PublicationViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'publications', PublicationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),  # подключаем urls приложения blog
     re_path(r'^auth/', include('djoser.urls')),
     re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
     (...),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
