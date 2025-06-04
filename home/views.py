from django.shortcuts import render
from shows.models import Show
from datetime import datetime

def homepage(request):
    shows = Show.objects.all()
    
    # Get all unique dates (for dropdown or filtering)
    available_dates = Show.objects.order_by('date').values_list('date', flat=True).distinct()

    # Filtering logic
    date = request.GET.get('date')
    show_type = request.GET.get('type')
    city = request.GET.get('city')
    price = request.GET.get('price')

    if date:
        try:
            parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
            shows = shows.filter(date=parsed_date)
        except ValueError:
            pass  # Ignore invalid date format

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

    return render(request, 'home/home.html', {
        'shows': shows,
        'available_dates': available_dates,
    })
