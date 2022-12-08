from django.urls import path

from assignment4app import views

app_name = 'assignment4app'

urlpatterns = [

    path('', views.index, name='index'),
    path('movie/<int:movie_id>/', views.detail, name='detail'),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]
