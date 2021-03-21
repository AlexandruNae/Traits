from django.urls import path, include
from rest_framework import routers
from . import views
from .views import UserViewSet, PostViewSet

router = routers.DefaultRouter()
router.register('users',UserViewSet)
router.register('posts',PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('iubire', views.show_html),
    path('index', views.index),
    path('home', views.home),
    path('formular', views.formular),
    path('user_list', views.user_list),
    path('my_user_wall/',views.my_user_wall),

    path('wall',views.wall2),

    # path('wall/<int:user_id',views.index, name = 'index'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('wall/<int:user_id>', views.wall, name='wall'),
    path('add/', views.add_1),
    path('logout_user/', views.logout_user),
    path('delete_post/<int:post_id>',views.delete_post, name='delete_post'),
    # path('delete_post',views.delete),

]
