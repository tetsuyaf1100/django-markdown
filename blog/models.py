from django.db import models

# Create your models here.
from django.db import models
from markdownx.models import MarkdownxField
from django.utils.safestring import mark_safe
from markdownx.utils import markdownify

class Blog(models.Model):
    title = models.CharField('タイトル', max_length=50)
    #text = models.TextField('テキスト')
    text = MarkdownxField('テキスト')
    created_at = models.DateField('作成日', auto_now_add=True)
    updated_at = models.DateField('更新日', auto_now=True)

    """ カスタムメソッド """
    def get_text_markdownx(self):
        return mark_safe(markdownify(self.text))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ブログ'
        verbose_name_plural = 'ブログ'
