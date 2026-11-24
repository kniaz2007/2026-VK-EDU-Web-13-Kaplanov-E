from django.db import models
from django.contrib import auth
from .managers import QuestionManager, AnswerManager, TagManager
from django.urls import reverse
User = auth.get_user_model()

class DefaultModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

class Tag(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    objects = TagManager()

class Question(DefaultModel):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=4095)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, related_name='questions')
    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
    def __str__(self):
        return self.title
    objects = QuestionManager()
    def get_my_url(self):
        return reverse('one_question', kwargs = {'question_id':self.id, })

class Answer(DefaultModel):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=4095)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
    def __str__(self):
        return f"ответ пользователя {self.author} на вопрос {self.question}"
    objects = AnswerManager()
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, verbose_name = "Пользователь")
    avatar = models.CharField(max_length=255)
    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

class QuestionLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'question'], name = 'unique_user_question_like')
        ]
        verbose_name = "Лайк вопроса"
        verbose_name_plural = "Лайки воспросов"
    def __str__(self):
        return f"Лайк пользователя {self.user} на вопрос {self.question}"

class AnswerLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'answer'], name = 'unique_user_answer_like')
        ]
        verbose_name = "Лайк ответа"
        verbose_name_plural = "Лайки ответов"
    def __str__(self):
        return f"Лайк пользователя {self.user} на ответ {self.answer}"




