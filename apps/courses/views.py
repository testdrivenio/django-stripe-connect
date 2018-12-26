import json

import stripe

from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.conf import settings
from django.views import View
from django.http import JsonResponse

from .models import Course


class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CourseListView, self).get_context_data(*args, **kwargs)
        return context

    def render_to_response(self, context, **response_kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(CourseListView, self).render_to_response(context, **response_kwargs)


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CourseDetailView, self).get_context_data(*args, **kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

    def render_to_response(self, context, **response_kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super(CourseDetailView, self).render_to_response(context, **response_kwargs)


class CourseChargeView(View):

    def post(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        json_data = json.loads(request.body)
        try:
            charge = stripe.Charge.create(
                amount=json_data['amount'],
                currency='usd',
                source=json_data['token'],
                description=json_data['description'],
            )
            if charge:
                return JsonResponse({'status': 'success'}, status=202)
        except stripe.error.StripeError as e:
            return JsonResponse({'status': 'error'}, status=500)
