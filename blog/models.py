from __future__ import unicode_literals     # For python 2.x

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from django.core.urlresolvers import reverse

from tagging.fields import TagField

# Create your models here.


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField('TITLE', max_length=100)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True,
                            help_text='one word for title alias')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True,
                                   help_text='simple description text')
    content = models.TextField('CONTENT')

    tag = TagField()        # tagging 모듈의 자체 Field (Default max_length=255, Blank=True)

    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)


    class Meta: # 필드 속성 외 ORM 처리를 위해 필요한 파라메터 정의
        verbose_name = 'post'           # 단수 별칭
        verbose_name_plural = 'posts'   # 복수 별칭
        db_table = 'my_post'            # DB에 저장되는 실제 테이블 이름, 생략시 '앱명_모델클래스명'을 테이블 명으로 지정
        ordering = ('-modify_date',)    # 정렬기준 modify_date 내림차순

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous_post(self):
        print("hear~!!! previous")
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        print("hear~!!! next")
        return self.get_next_by_modify_date()