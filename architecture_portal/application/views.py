from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages

from application.forms import PriceCalculatorForm, ApplicationForm
from application.models import Application


def calculate_price(request):
    if request.method == 'POST':
        form = PriceCalculatorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Base price calculation logic
            base_price_per_sqm = 50  # Adjust this value as needed
            complexity_multiplier = {
                'simple': 1.0,
                'medium': 1.3,
                'complex': 1.7
            }[data['design_complexity']]

            floors_multiplier = 1 + (data['floors'] - 1) * 0.2

            # Calculate base price
            total_price = (data['square_meters'] * base_price_per_sqm *
                           complexity_multiplier * floors_multiplier)

            # Add additional services
            additional_services_price = 0
            if '3d' in data['additional_services']:
                additional_services_price += data['square_meters'] * 10
            if 'interior' in data['additional_services']:
                additional_services_price += data['square_meters'] * 15
            if 'permit' in data['additional_services']:
                additional_services_price += 500
            if 'construction' in data['additional_services']:
                additional_services_price += total_price * 0.1

            total_price += additional_services_price

            # For AJAX requests
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'square_meters': data['square_meters'],
                    'floors': data['floors'],
                    'design_complexity': dict(form.fields['design_complexity'].choices)[data['design_complexity']],
                    'additional_services': [dict(form.fields['additional_services'].choices)[s] for s in
                                            data['additional_services']],
                    'total_price': round(total_price, 2)
                })

            # For regular form submission
            return render(request, 'result.html', {
                'form': form,
                'total_price': round(total_price, 2),
                'calculation_data': data
            })
    else:
        form = PriceCalculatorForm()

    return render(request, 'calculator.html', {'form': form})


class ApplicationCreateView(CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'application_form.html'
    success_url = reverse_lazy('application:thank_you')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Your application has been submitted successfully!')
        return response
