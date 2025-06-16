
# ---------------------------------------------------------------------------- #

from django.shortcuts import render
from django.views import generic

# ---------------------------------------------------------------------------- #

class HomeView(generic.View):
    template_name = 'public/home.html'
    context = {}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
    
def dashboard_home(request):
    users = [
        {'name': 'Juan', 'age': 30, 'country': 'México'},
        {'name': 'Ana', 'age': 25, 'country': 'Colombia'},
        {'name': 'Luis', 'age': 28, 'country': 'Perú'},
    ]
    chart_data = [12, 5, 8]
    return render(request, 'dashboard/home.html', {
    'users': users,
    'chart_data': chart_data,
})

# ---------------------------------------------------------------------------- #