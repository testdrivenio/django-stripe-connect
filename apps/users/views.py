import urllib

import requests

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import View
from django.conf import settings
from django.shortcuts import redirect

from .models import Seller


class StripeAuthorizeView(View):

    def get(self, request):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        url = 'https://connect.stripe.com/oauth/authorize'
        params = {
            'response_type': 'code',
            'scope': 'read_write',
            'client_id': settings.STRIPE_CONNECT_CLIENT_ID,
            'redirect_uri': f'http://localhost:8000/users/oauth/callback'
        }
        url = f'{url}?{urllib.parse.urlencode(params)}'
        return redirect(url)


class StripeAuthorizeCallbackView(View):

    def get(self, request):
        code = request.GET.get('code')
        if code:
            data = {
                'client_secret': settings.STRIPE_SECRET_KEY,
                'grant_type': 'authorization_code',
                'client_id': settings.STRIPE_CONNECT_CLIENT_ID,
                'code': code
            }
            url = 'https://connect.stripe.com/oauth/token'
            resp = requests.post(url, params=data)
            # add stripe info to the seller
            stripe_user_id = resp.json()['stripe_user_id']
            stripe_access_token = resp.json()['access_token']
            seller = Seller.objects.filter(user_id=self.request.user.id).first()
            seller.stripe_access_token = stripe_access_token
            seller.stripe_user_id = stripe_user_id
            seller.save()
        url = reverse('home')
        response = redirect(url)
        return response
