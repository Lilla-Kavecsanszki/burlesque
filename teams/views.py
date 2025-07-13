from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Team
from shows.models import Show

def chunked(queryset, size):
    """Chunk any list or queryset into evenly-sized chunks."""
    return [queryset[i:i + size] for i in range(0, len(queryset), size)]

def teams_list(request):
    starts_with = request.GET.get("starts_with")
    team_type = request.GET.get("type")
    city = request.GET.get("city")
    price = request.GET.get("price")

    teams = Team.objects.all()
    available_cities = Team.objects.order_by('city').values_list('city', flat=True).distinct()

    # Apply filters
    if starts_with:
        teams = teams.filter(name__istartswith=starts_with)
    if team_type:
        teams = teams.filter(show_type__iexact=team_type)
    if city:
        teams = teams.filter(city__iexact=city)
    if price:
        try:
            price = float(price)
            teams = teams.filter(price__lte=price)
        except (ValueError, TypeError):
            pass

    # Paginate teams
    paginator = Paginator(teams, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Shows for carousel (chunked into groups of 4)
    all_shows = Show.objects.filter(featured_on_homepage=True).order_by('-date')
    show_groups = chunked(list(all_shows), 4)

    return render(request, 'teams/teams_list.html', {
        'page_obj': page_obj,
        'starts_with': starts_with,
        'available_cities': available_cities,
        'show_groups': show_groups,  
    })

# Team detail view
def team_details(request, pk):
    team = get_object_or_404(Team, pk=pk)
    shows = Show.objects.filter(featured_on_homepage=True).order_by('date')
    return render(request, 'teams/team_details.html', {
        'team': team,
        'shows': shows,
    })
