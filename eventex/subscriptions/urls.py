# coding: utf-8
from django.conf.urls import patterns, url
from eventex.subscriptions.views import SubscriptionCreateView, SubscriptionDetailView

urlpatterns = patterns('eventex.subscriptions.views',
                       url(r'^$', SubscriptionCreateView.as_view(), name='subscribe'),
                       url(r'^(?P<pk>\d+)/$', SubscriptionDetailView.as_view(), name='detail'),
)