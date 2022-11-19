from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('user/<int:pk>', views.UserDetailView.as_view(template_name='users/user-detail.html'),
         name='record-detail'),
    path('<int:pk>/update-data-user/', views.UpdateUserView.as_view(template_name="updateDataUser.html"),
         name='update-data-user'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)