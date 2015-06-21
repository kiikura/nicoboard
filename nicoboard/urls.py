# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.authtoken import views as tokenview

from nicoboard import views

router = routers.DefaultRouter()
router.register(r'boards', views.BoardViewSet)
router.register(r'msgs', views.MessageViewSet)

urlpatterns = patterns('',
  url(r'^$', TemplateView.as_view(template_name="nicoboard/index.html"), name="nicoboard"),
  url(r'^api/', include(router.urls)),
#  url(r'^board/', BoardIndexView.as_view()),
  url(r'^board/(?P<slug>\w+)/', views.BoardDetailView.as_view()),
#  url(r'^monitor/', MonitorIndexView.as_view()),
  url(r'^monitor/(?P<slug>\w+)/', views.MonitorDetailView.as_view()),
)


urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]


urlpatterns += [
    url(r'^api-token-auth/', tokenview.obtain_auth_token)
]
