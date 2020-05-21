from django.contrib import admin

# Register your models here.
from .models import Choice, Question


# admin.site.register(Choice)
# 创建“投票”对象时直接添加好几个选项
# class ChoiceInline(admin.StackedInline):
# 表格式的单行显示关联对象，而不是纵向罗列
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# admin.site.register(Question)

class QuestionAdmin(admin.ModelAdmin):
	# fields = ['pub_date', 'question_text']
	fieldsets = [
		(None,               {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date']}),
	]
	# 显示单个字段
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)


