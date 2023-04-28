from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as auth_views

from . import views

router = routers.DefaultRouter()
router.register('category', views.CategoryViewSet)
router.register('item', views.ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user_info/', views.get_user_info),
    path('register/', views.user_register),
    path('auth_token/', auth_views.obtain_auth_token),
    path('auth/', include('rest_framework.urls')),
]


#     path('category/', views.CategoryViewSet.as_view(
#         {'get':'list', 'post':'create'}
#     )),
#     path('item/', views.ItemViewSet.as_view(
#         {'get': 'list', 'post': 'create'}
#     )),
#     # path('category/<int:pk>/', views.CategoryViewSet.as_view())
# ]