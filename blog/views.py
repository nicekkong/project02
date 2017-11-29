from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from blog.models import Post
from .forms import PostSearchForm

from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList

class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'  # 템플릿 파일 이름 (default => blog/post_list.html)
    context_object_name = 'posts'     # default => object_list
    paginate_by = 2                   # 페이징 기능 / 한페이지에 2개씩


class PostDV(DetailView):
    model = Post


class PostAV(ArchiveIndexView):  # ArchiveIndexView : 객체에서 날짜 기준으로 출력
    model = Post
    date_field = 'modify_date'     # default template 이름은 '모델클래스소문자_archive.html'


class PostYAV(YearArchiveView):
    model = Post                # default template 이름은 '모델클래스소문자_archive_year.html'
    date_field = 'modify_date'  # 정렬의 기준이 되는 필드 'modify_date'
    make_object_list = True     # 해당 년도에 해당하는 객체의 리스트를 만들어 템플릿으로 전달한다.


class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_date'
    month_format = '%m'


class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_date'


class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'


class TagTV(TemplateView):
    template_name = "tagging/tagging_cloud.html"


class PostTOL(TaggedObjectList):
    model = Post
    template_name = 'tagging/tagging_post_list.html'


class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form):
        print("12312312312")
        schWord = '%s' % (self.request.POST['search_word'])

        post_list = Post.objects.filter(Q(title__icontains=schWord) |
                                        Q(description__icontains=schWord) |
                                        Q(content__icontains=schWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)