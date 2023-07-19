from django.shortcuts import redirect
from django.urls import reverse

class CsrfMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Check if the response contains the CSRF failure message
        if 'CSRF verification failed. Request aborted.' in response.content.decode('utf-8'):
            # Redirect to the login page or a custom error page
            return redirect(reverse(''))  # Replace 'login_url_name' with your actual login URL name

        return response
