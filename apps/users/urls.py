from django.urls import path

from .views import StripeAuthorizeView, StripeAuthorizeCallbackView


urlpatterns = [
  path('authorize/', StripeAuthorizeView.as_view(), name='authorize'),
  path('oauth/callback/', StripeAuthorizeCallbackView.as_view(), name='authorize_callback'),
]
