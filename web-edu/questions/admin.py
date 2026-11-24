from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from questions.models import Question, Answer, UserProfile, QuestionLike, AnswerLike, Tag

User = get_user_model()

class NewUserAdmin(UserAdmin):
    class UserInline(admin.StackedInline):
        model = UserProfile
        extra = 0
    def get_username(self, obj):
        return obj.username
    get_username.short_description = "Пользователь"
    def get_email(self, obj):
        return obj.email
    search_fields = ['username']
    get_email.short_description = "Логин"
    list_display = ['get_username', 'get_email']
    inlines = [UserInline]

class NewQuestionAdmin(admin.ModelAdmin):
    class AnswerInline(admin.TabularInline):
        model = Answer
        extra = 0
    raw_id_fields = ['author']
    search_fields = ['title']
    list_display = ['title', 'author', 'created_at']
    inlines = [AnswerInline]
    list_filter = ['is_active', 'created_at']
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('author', )

class NewAnswerAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'question', 'author']
    search_fields = ['title']
    list_filter = ['is_active', 'created_at']
    raw_id_fields = ['author', 'question']
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('author', 'question')

class QuestionLikeAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user', 'question']
    raw_id_fields = ['user', 'question']
    search_fields = ['user__username']
    list_filter = ['question']
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user', 'question')

class AnswerLikeAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user', 'answer']
    raw_id_fields = ['user', 'answer']
    search_fields = ['user__username']
    list_filter = ['answer']
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user', 'answer')
admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)
admin.site.register(Question, NewQuestionAdmin)
admin.site.register(Answer, NewAnswerAdmin)
admin.site.register(QuestionLike, QuestionLikeAdmin)
admin.site.register(AnswerLike, AnswerLikeAdmin)
admin.site.register(Tag)
