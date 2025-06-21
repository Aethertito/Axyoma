
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

    # 🔐 Simulando niveles: 'admin', 'editor', 'viewer'
    user_level = 'admin'  # Aquí podrías hacer algo como: request.user.profile.level

    # 📦 Opciones de menú por nivel
    menu_options_by_level = {
        'admin': [
            {'label': 'Panel de Control', 'url': '/dashboard/'},
            {'label': 'Usuarios', 'url': '/dashboard/users/'},
            {'label': 'Configuraciones', 'url': '/dashboard/settings/'},
        ],
        'editor': [
            {'label': 'Panel de Control', 'url': '/dashboard/'},
            {'label': 'Entradas', 'url': '/dashboard/posts/'},
        ],
        'viewer': [
            {'label': 'Panel de Control', 'url': '/dashboard/'},
        ],
    }

    menu_options = menu_options_by_level.get(user_level, [])

    return render(request, 'dashboard/home.html', {
        'users': users,
        'chart_data': chart_data,
        'menu_options': menu_options,
    })


# ---------------------------------------------------------------------------- #