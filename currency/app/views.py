from django.shortcuts import render
import requests


def index(request):
    response = requests.get(
        url='https://api.exchangerate-api.com/v4/latest/USD').json()
    currency = response.get('rates')

    if request.method == 'GET':
        context = {
            'currency': currency
        }
        return render(
            request=request,
            template_name='app_templates/index.html',
            context=context
        )

    if request.method == 'POST':
        amount_str = request.POST.get('amount')
        try:
            amount = float(amount_str)
        except ValueError:
            amount = 0.0
        from_curr = request.POST.get('from')
        to_curr = request.POST.get('to')
        converter = round(
            (currency[to_curr] / currency[from_curr]) * amount, 2)
        context = {
            'currency': currency,
            'converter': converter
        }
        return render(
            request=request,
            template_name='app_templates/index.html',
            context=context
        )
