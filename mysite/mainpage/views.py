from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView


class MainPageView(TemplateView):

    template_name = "mainpage/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context
        #return render(request, 'mainpage/index.html', {'title': 'Главная Страница'})
