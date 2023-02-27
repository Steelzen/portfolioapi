from django.urls import path
from . import views

urlpatterns = [
    path('aboutme/list', views.AboutMeList.as_view(), name="aboutmelist"),
    path('aboutme/list/<int:pk>', views.AboutMeDetail.as_view(), name="aboutmedetail"),
    path('aboutme/update/<int:pk>', views.AboutMeUpdate.as_view(), name="aboutmeupdate"),
    path('project/list', views.ProjectList.as_view(), name="projectlist"),
    path('project/list/<int:pk>', views.ProjectDetail.as_view(), name="projectdetail"),
    path('project/create', views.ProjectCreate.as_view(), name="projectcreate"),
    path('project/update/<int:pk>', views.ProjectUpdate.as_view(), name="projectupdate"),
    path('project/delete/<int:pk>', views.ProjectDelete.as_view(), name="projectdelete"),
]