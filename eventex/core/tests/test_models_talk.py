# coding: utf-8
from django.test import TestCase
from eventex.core.models import Talk, PeriodManager, Course


class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(title=u'Introdução ao Django',
                                        description=u'Descrição da Palestra',
                                        start_time='10:00')
        
    def test_create(self):
        'Deve criar um registro'
        self.assertEqual(1, self.talk.pk)
        
    def test_unicode(self):
        'Unicode deve ser igual ao title'
        self.assertEqual(u'Introdução ao Django', unicode(self.talk))
        
    def test_create_speakers(self):
        'Uma palestra pode ter um ou mais palestrantes'
        self.talk.speakers.create(name='Henrique Bastos',
                                  slug='henrique-bastos',
                                  url='http://henriquebastos.net')
        
        self.assertEqual(1, self.talk.speakers.count())
        
    def test_period_manager(self):
        'Manager default deve ser PeriodManager'
        self.assertIsInstance(Talk.objects, PeriodManager)
        
class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(title=u'Tutorial Django',
                                            description=u'Descrição do Curso',
                                            start_time='10:00', slots=20)
        
    def test_create(self):
        'Deve criar um registro'
        self.assertEqual(1, self.course.pk)
        
    def test_unicode(self):
        'Unicode deve ser igual ao title'
        self.assertEqual(u'Tutorial Django', unicode(self.course))
        
    def test_create_speakers(self):
        'Um curso pode ter um ou mais speakers'
        self.course.speakers.create(name='Henrique Bastos',
                                    slug='henrique-bastos',
                                    url='http://henriquebastos.net')
        
        self.assertEqual(1, self.course.speakers.count())
        
    def test_period_manager(self):
        'Manager default deve ser PeriodManager'
        self.assertIsInstance(Course.objects, PeriodManager)