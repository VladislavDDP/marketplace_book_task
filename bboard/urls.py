from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView.as_view(), name='home'),
    path('<int:rubric_id>/', views.byRubricView.as_view(), name='rubric'),
    path('add/', views.BbCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', views.PostView.as_view(), name='detail'),
    path('edit/<int:pk>/', views.BbEditview.as_view(), name='edit'),
    path('delete/<int:pk>/', views.BbDeleteView.as_view(), name='delete'),
]
