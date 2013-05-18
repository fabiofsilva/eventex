# coding: utf-8
from django.views.generic import TemplateView, DetailView
from models import Speaker, Talk

class HomePageView(TemplateView):
    template_name = 'index.html'

class SpeakerDetailView(DetailView):
    model = Speaker
    
class TalkListVew(TemplateView):
    template_name = 'core/talk_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(TalkListVew, self).get_context_data(**kwargs)
        context.update({'morning_talks': Talk.objects.at_morning(),
                        'afternoon_talks': Talk.objects.at_afternoon(),})
        return context
    
class TalkDetailView(DetailView):
    model = Talk