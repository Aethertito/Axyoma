
# ---------------------------------------------------------------------------- #

from django.shortcuts import render
from django.views import generic

# ---------------------------------------------------------------------------- #

class HomeView(generic.View):
    template_name = 'public/index.html'

    def get(self, request, *args, **kwargs):
        section = request.GET.get('section', 'inicio')
        if section == 'seccion1':
            content = "Aquí va algo de la Sección 1."
        elif section == 'seccion2':
            content = "Aquí va algo de la Sección 2."
        else:
            content = "Aquí va la landing general."
        context = { 'section': section, 'content': content }
        return render(request, self.template_name, context)

# ---------------------------------------------------------------------------- #