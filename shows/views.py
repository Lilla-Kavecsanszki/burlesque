from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Show

def shows_list(request):
    starts_with = request.GET.get("starts_with")
    shows = Show.objects.all()

    if starts_with:
        shows = shows.filter(title__istartswith=starts_with)

    paginator = Paginator(shows, 8)  # 8 items per page (2 rows x 4 per row)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'shows/shows_list.html', {
        'page_obj': page_obj,
        'starts_with': starts_with,
    })
