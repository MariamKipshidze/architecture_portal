from django.shortcuts import render
from django.views.generic import ListView

from about_us.models import TeamMember


def contact_view(request):
    return render(request, 'contact.html')


class TeamListView(ListView):
    model = TeamMember
    template_name = 'team_list.html'
    context_object_name = 'team_members'

    def get_queryset(self):
        return TeamMember.objects.filter(is_active=True).order_by('order')
