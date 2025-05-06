from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# public pages
class RegisterPageView(TemplateView):
    template_name = 'register.html'

class LoginPageView(TemplateView):
    template_name = 'login.html'

class DepositFormPageView(TemplateView):
    template_name = 'deposit_form.html'

class DepositListPageView(TemplateView):
    template_name = 'deposit_list.html'

# protected page (requires login)
class NewDepositPageView(LoginRequiredMixin, TemplateView):
    template_name = 'new_deposit.html'
    # optional: where to redirect if not logged in
    login_url = '/login/'  
    # optional: query‑string param name for “next”
    redirect_field_name = 'next'