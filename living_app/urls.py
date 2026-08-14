from django.urls import path
from living_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("",views.index,name="index"),
    path("pg/",views.pg_view,name="pg"),
    path("pg/<int:id>/",views.pg_inte_view,name="pg_details"),
    path("colive/",views.coliv_view,name="colive"),
    path("colive/<int:id>/",views.coliv_inte_view,name="coliv_details"),
    path("homes/",views.homes_view,name="homes"),
    path("homes/<int:id>/",views.home_inte_view,name="home_details")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)