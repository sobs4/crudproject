# from django.urls import path
# from. import views

# urlpatterns = [
# path('',views.learn_django,name='courseone'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),  # New path for base URL
    path('add_course/', views.add_course, name='add_course'),
    path('add_tutor/', views.add_tutor, name='add_tutor'),
    path('show_courses/', views.show_courses, name='show_courses'),
    path('show_tutors/', views.show_tutors, name='show_tutors'),
    path('search_courses/', views.search_courses, name='search_courses'),
    
]