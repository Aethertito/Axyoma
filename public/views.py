
# ---------------------------------------------------------------------------- #

from django.shortcuts import render
from django.views import generic

# ---------------------------------------------------------------------------- #

class HomeView(generic.View):
    template_name = 'public/home.html'
    context = {}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

# ---------------------------------------------------------------------------- #