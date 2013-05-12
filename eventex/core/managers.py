# coding: utf-8
from datetime import time
from django.db import models
    
class KindContactManager(models.Manager):
    def __init__(self, kind):
        super(KindContactManager, self).__init__()
        self.kind = kind
        
    def get_query_set(self):
        queryset = super(KindContactManager, self).get_query_set()
        queryset = queryset.filter(kind=self.kind)
        return queryset
    
class PeriodManager(models.Manager):
    midday = time(12)
    
    def at_morning(self):
        queryset = self.filter(start_time__lt=self.midday).order_by('start_time')
        return queryset
    
    def at_afternoon(self):
        queryset = self.filter(start_time__gte=self.midday).order_by('start_time') 
        return queryset               