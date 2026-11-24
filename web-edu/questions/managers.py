from django.db import models
from django.db.models import Count

class TagManager(models.Manager):
    def popular(self):
        return self.annotate(
            question_count=Count('questions') 
            ).order_by('-question_count')[:12]
class QuestionManager(models.Manager):
    def new(self):
        return self.filter(is_active=True).prefetch_related('tags').order_by('-created_at').annotate(
            likes_count=Count('questionlike'),
            answers_count=Count('answer', distinct=True)
        )
    def best(self):
        return self.filter(is_active=True).prefetch_related('tags').annotate(
            likes_count=Count('questionlike')
        ).order_by('-likes_count')
    def by_tag(self, tag_name):
        return self.filter(tags__name=tag_name, is_active=True).select_related('author').prefetch_related('tags').annotate(
            likes_count=Count('questionlike')
        )
class AnswerManager(models.Manager):
    def new(self):
        return self.filter(is_active=True).select_related('author').order_by('-created_at').annotate(
            likes_count=Count('answerlike')
        )
    def best(self):
        return self.filter(is_active=True).annotate.annotate(
            likes_count=Count('answerlike')
        ).select_related('author').order_by('-likes_count')