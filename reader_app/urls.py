from django.urls import include, path
from rest_framework import routers

from .views import *
from .views import CategoryViewSet, RecipeViewSet, UserViewSet

# urlpatterns  = [
#     path('recipes/', RecipeViewSet.as_view({'get': 'list', 'post': 'create'}), name='recipe-list'),
#     path('recipes/<int:pk>/', RecipeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='recipe-detail'),
#     path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
#     path('users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-detail'),
#     path('categories/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-list'),
#     path('categories/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='category-detail'),
# ]

router = routers.DefaultRouter()
router.register(r"recipes", RecipeViewSet, basename="recipe")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"users", UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
