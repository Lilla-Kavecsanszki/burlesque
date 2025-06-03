from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Show

def shows_list(request):
    shows = Show.objects.all()  # You can apply filters here
    paginator = Paginator(shows, 8)  # 8 items per page (2 rows x 4 per row)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'shows/shows_list.html', {'page_obj': page_obj})
