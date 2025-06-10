from django.contrib import admin
from django.urls import path, include
from main.views import index, view_redirect, wiki, edit

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # 입력 form
    path('redirect_search/', view_redirect, name='redirect_view'),
    path('<str:name>/', wiki, name='wiki'),
    path('<str:name>/edit/', edit, name='edit'),
]

# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
