from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register.as_view(), name='register'),
    path('ongoing_to_do_list/', views.todo, name='todo'),
    path('completed_to_do_list/', views.andtodo, name='andtodo'),
    path('add_to_do_list/', views.addtodo, name='addtodo'),
    path('delete_ongoing_task/<int:id>/', views.delete, name='delete'),
    path('delete_completed_task/<int:id>/', views.deletetodo, name='deletetodo'),
    path('complete_ongoing_task/<int:id>/', views.change, name='change'),
    path('reverse_completed_task/<int:id>/', views.changer, name='changer'),
    path('terms_of_service/', views.term, name='term'),
    path('privacy_policy/', views.privacy, name='privacy')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)