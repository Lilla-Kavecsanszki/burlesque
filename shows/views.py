from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Show

def shows_list(request):
    starts_with = request.GET.get("starts_with")
    show_type = request.GET.get("type")
    city = request.GET.get("city")
    price = request.GET.get("price")

    shows = Show.objects.all()
    
    available_cities = Show.objects.order_by('city').values_list('city', flat=True).distinct()

    if starts_with:
        shows = shows.filter(title__istartswith=starts_with)

    if show_type:
        shows = shows.filter(show_type__iexact=show_type)

    if city:
        shows = shows.filter(city__icontains=city)

    if price:
        try:
            price = float(price)
            shows = shows.filter(price__lte=price)
        except ValueError:
            pass

    paginator = Paginator(shows, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'shows/shows_list.html', {
        'page_obj': page_obj,
        'starts_with': starts_with,
        'show_type': show_type,
        'city': city,
        'available_cities': available_cities,
        'price': price,
    })
