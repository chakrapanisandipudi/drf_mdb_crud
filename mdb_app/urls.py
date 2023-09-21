from django.urls import path
from mdb_app import views

urlpatterns = [
    path('api/tutorials/', views.tutoriallist, name="tutoriallist"),
    path('api/tutorials/<int:pk>', views.tutorial_detail, name="tutorial_detail"),
    path('api/tutorials/published/', views.tutorial_list_published, name="tutorial_list_published")
]