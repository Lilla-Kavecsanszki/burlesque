from django.shortcuts import render
from shows.models import Show
from datetime import datetime

def homepage(request):
    shows = Show.objects.all()
    available_dates = Show.objects.order_by('date').values_list('date', flat=True).distinct()
    available_cities = Show.objects.order_by('city').values_list('city', flat=True).distinct()

    date = request.GET.get('date')
    show_type = request.GET.get('type')
    city = request.GET.get('city')
    price = request.GET.get('price')

    filtered = any([date, show_type, city, price])

    if filtered:
        if date:
            try:
                parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
                shows = shows.filter(date=parsed_date)
            except ValueError:
                pass

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
    else:
        # Show up to 4 promoted shows
        shows = Show.objects.filter(featured_on_homepage=True).order_by('-date')[:4]

    return render(request, 'home/home.html', {
        'shows': shows,
        'available_dates': available_dates,
        'available_cities': available_cities,
    })
