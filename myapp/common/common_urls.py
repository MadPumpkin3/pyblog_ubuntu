from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from . import common_views as views
from django.urls import path

app_name = "common"

urlpatterns = [
    # path("", views.Index.as_view(), name="first_index"), -- 추후에 수정
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))),
    path("mailsend.do", views.NaverOutboundMailer.as_view(), name="nvOutboundMailer"),
]