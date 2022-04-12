from unicodedata import name
from django.urls import path
from . import views
from django.conf import settings
from edu_library.settings import DEBUG,STATIC_ROOT,STATIC_URL,MEDIA_ROOT,MEDIA_URL
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index,name='index'),
    path('upload/',views.upload, name='upload-book'),
    path('update/<int:book_id>',views.update_book,),
    path('delete/<int:book_id>',views.delete_book),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''if DEBUG:
    urlpatterns += static(STATIC_URL,document_root = STATIC_ROOT),
    urlpatterns += static(MEDIA_URL,document_root = MEDIA_ROOT),'''