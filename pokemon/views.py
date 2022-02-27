import django


from django.views.generic import TemplateView


class HomePageView(TemplateView):
  template_name = 'home.html'   # uses django provided template view to show home.html content


class AboutView(TemplateView):
  template_name = 'about.html'

class InfoView(TemplateView):
  template_name = 'info.html'