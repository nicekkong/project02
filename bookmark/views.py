from django.shortcuts import render
from django.views.generic import ListView, DetailView

from bookmark.models import Bookmark

# Create your views here.

class BookMarkLV(ListView):
    model = Bookmark

class BookMarkDV(DetailView):
    model = Bookmark