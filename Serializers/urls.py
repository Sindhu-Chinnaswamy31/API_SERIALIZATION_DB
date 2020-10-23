from django.urls import path
from Serializers import views

app_name="Serializers"

urlpatterns = [
    path('serializers/',views.HelloApiView.as_view(),name="Hello API"),
    path('serializers_db/',views.HelloApiView_1.as_view(),name="Hello API 1"),
    path('serializers_db/<int:pk>',views.HelloApiView_2.as_view(),name="Hello API 2"),
]