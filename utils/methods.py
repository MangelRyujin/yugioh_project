from django.core.paginator import Paginator

def _get_paginator(request, object):
    paginator = Paginator(object, 100)
    page_number = request.GET.get('page', 1)
    page_object = paginator.get_page(page_number)
    
    context = {
        'paginator': page_object
    }
    
    return context