
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('account.urls')),
    path('comments/', views.CommentListCreateView.as_view()),
    path('comments/<int:pK>/', views.CommentDetaileView.as_view())


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
