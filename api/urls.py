#from xml.etree.ElementInclude import include
from django.urls import path, include # type: ignore
from . import views
from rest_framework.routers import DefaultRouter # type: ignore


router = DefaultRouter() # type: ignore
router.register('employees', views.EmployeeViewset, basename='employeedir')




urlpatterns = [
    path('students/', views.studentsView),  
    path('students/<int:pk>/', views.studentDetailView), 
    #path('employees/', views.Employees.as_view()),  
    #path('employees/<int:pk>/', views.EmployeeDetail.as_view())  
    path('', include(router.urls)),
    path('blogs/', views.BlogsView.as_view()),
    path('comments/', views.CommentsView.as_view()),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),
    path('albums/', views.AlbumView.as_view()),
    path('tracks/', views.TrackView.as_view())

]

