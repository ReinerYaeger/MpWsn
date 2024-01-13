from django.shortcuts import render, redirect

# from sms.forms import SignupForm
#from django.contrib.gis.geos import Point


def index(requests):
    return render(requests, 'sms/index.html')


def experiment(requests):
    return render(requests, 'sms/experiment.html')


def live_analytics(requests):
    context = {

    }
    return render(requests, 'sms/technique/live_analytics.html', context)


def experiment_results(requests):
    context = {

    }
    return render(requests, 'sms/technique/live_analytics.html', context)


def map_view(requests,parish=None):
    context = {

    }

    if parish is not None:
        print(1)

    return render(requests, 'sms/map/jamaica.html', context)

# class CustomLoginView(LoginView):
# 	template_name = 'sms/login.html'
#
# 	class CustomLogoutView(LogoutView):
# 		next_page = reverse_lazy('login')  # 'login' should be replaced with the name of your login URL
#
# 		def get_next_page(self):
# 			# Customize this method if needed
# 			return self.next_page
#
# 		def dispatch(self,  requests, *args, **kwargs):
# 			response = super().dispatch( requests, *args, **kwargs)
# 			return response
#
# 	def form_valid(self, form):
# 		"""If the form is valid, perform login and redirect."""
# 		login(self. requests, form.get_user())
# 		return redirect('index')  # Adjust the redirect URL
#
# 	def form_invalid(self, form):
# 		"""If the form is invalid, render the invalid form."""
# 		return self.render_to_response(self.get_context_data(form=form))
#
#
# class CustomLogoutView(LogoutView):
# 	next_page = reverse_lazy('index')
#
# 	def get_next_page(self):
# 		return self.next_page
#
# 	def dispatch(self,  requestss, *args, **kwargs):
# 		response = super().dispatch( requestss, *args, **kwargs)
# 		return response
#
#
# def signup_view( requests):
# 	if  requests.method == 'POST':
# 		form = SignupForm( requests.POST)
# 		if form.is_valid():
# 			form.save()
# 			# Redirect to a success page or login page
# 			return redirect('login')  # You can adjust the redirect URL
# 	else:
# 		form = SignupForm()
#
# 	return render( requests, 'sms/signup.html', {'form': form})
