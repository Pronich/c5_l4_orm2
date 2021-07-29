from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, TagLink

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        select_main_section = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data['is_main']:
                select_main_section += 1
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
        if select_main_section < 1:
            raise ValidationError('Укажите основной раздел')
        if select_main_section > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()  # вызываем базовый код переопределяемого метода


class TaglinkInline(admin.TabularInline):
    model = TagLink
    formset = RelationshipInlineFormset
    extra = 0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        TaglinkInline,
    ]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass