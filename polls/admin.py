from django.contrib import admin

from .models import Question, Choice
# Register your models here.


class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')

    class Meta:
        model = Question


class ChoiceModelAdmin(admin.ModelAdmin):
    list_display = ('question', 'votes')

    class Meta:
        model = Choice

admin.site.register(Question, QuestionModelAdmin)
admin.site.register(Choice, ChoiceModelAdmin)
