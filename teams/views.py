from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Team

def teams_list(request):
    starts_with = request.GET.get("starts_with")
    teams = Team.objects.all()

    if starts_with:
        teams = teams.filter(name__istartswith=starts_with)

    paginator = Paginator(teams, 8)  # 8 items per page (2 rows x 4 per row)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'teams/teams_list.html', {
        'page_obj': page_obj,
        'starts_with': starts_with,
    })