from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'votes'
urlpatterns = [
    path('', views.index, name='index'),
    path('positioncreate/', views.position_create, name='position_create'),
    path('candidatecreate/', views.candidate_create, name='candidate_create'),
    path('<int:candidate_id>/', views.candidate_detail, name='candidate_detail'),
    path('<int:candidate_id>/vote', views.vote, name='vote'),
    path('<int:candidate_id>/candidateupdate', views.candidate_update, name='candidate_update')
]
