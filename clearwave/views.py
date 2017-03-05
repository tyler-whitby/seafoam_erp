import account.views

class SignupView(account.views.SignupView):
    template_name = 'clearwave/signup.html'

    super(SignupView, self).