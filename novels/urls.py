from django.urls import path
from . import views
from django.urls import path, include
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'novels', views.NovelViewSet)

urlpatterns = [
    #path('',views.getnovels,name="novels"),
    #path('novel/<str:pk>/',views.getnovel,name='get_novel'),
    #path('createnovel/',views.createnovel,name = 'create_novel'),
    #path('updatenovel/<str:pk>/',views.updatenovel,name='update_novel'),
    #path('deletenovel/<str:pk>/',views.deletenovel,name='delete_novel'),


    path('', include(router.urls)),

]