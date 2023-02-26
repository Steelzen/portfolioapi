from django.urls import path
from . import views

urlpatterns = [
    path('aboutme/list', views.AboutMeList.as_view(), name="aboutmelist"),
    path('aboutme/list/<int:pk>', views.AboutMeDetail.as_view(), name="aboutmedetail"),
    path('aboutme/update/<int:pk>', views.AboutMeUpdate.as_view(), name="aboutmeupdate"),
]