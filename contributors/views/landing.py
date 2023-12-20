from django.views.generic.base import TemplateView


class LandingView(TemplateView):
    """New landing view."""

    template_name = 'landing.html'
