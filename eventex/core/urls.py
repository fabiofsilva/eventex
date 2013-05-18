# coding: utf-8
from django.conf.urls import patterns, url
from eventex.core.views import HomePageView, TalkListVew, SpeakerDetailView, TalkDetailView

urlpatterns = patterns('eventex.core.views',
                       url(r'^$', HomePageView.as_view(), name='homepage'),
                       url(r'^palestrantes/(?P<slug>[\w-]+)/$', SpeakerDetailView.as_view(), name='speaker_detail'),                      
                       url(r'^palestras/', TalkListVew.as_view(), name='talk_list'),
                       url(r'^palestra/(?P<pk>\d+)/$', TalkDetailView.as_view(), name='talk_detail'),                                              
)