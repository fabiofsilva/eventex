# coding: utf-8
from django.contrib import admin
from models import Speaker, Contact, Talk, Course, Media

class ContactInLine(admin.TabularInline):
    model = Contact
    extra = 1
    
class MediaInLine(admin.TabularInline):
    model = Media
    extra = 1
    
class SpeakerAdmin(admin.ModelAdmin):
    inlines = [ContactInLine,]
    prepopulated_fields = {'slug': ('name',)}
    
class TalkAdmin(admin.ModelAdmin):
    inlines = [MediaInLine]
    
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Talk, TalkAdmin)
admin.site.register(Course)