from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import JsonResponse

from .utils import get_contragents_list


def index(request):
    if request.method == 'POST':
        try:
           search_string = request.POST['search']
        except KeyError:
            search_string = ''
        contragent = get_contragents_list(search_string=search_string)
        return JsonResponse(contragent)
    else:
        context = {}
        return render(request, 'common/index.html', context)

