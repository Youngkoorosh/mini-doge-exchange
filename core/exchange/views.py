from django.http import JsonResponse
from .models import Wallet
from .services import get_doge_price

def get_price(request):
    return JsonResponse({'price': get_doge_price()})

def get_wallet(request):
    wallet, _ = Wallet.objects.get_or_create(id=1)
    return JsonResponse({
        'usdt': wallet.balance_usdt,
        'doge': wallet.doge
    })


def buy_doge(request):
    wallet, _ = Wallet.objects.get_or_create(id=1)
    amount = float(request.GET.get('amount', 0))
    price = get_doge_price()

    if wallet.balance_usdt >= amount:
        wallet.doge += amount / price
        wallet.balance_usdt -= amount
        wallet.save()

    return JsonResponse({'status': 'ok'})


def sell_doge(request):
    wallet, _ = Wallet.objects.get_or_create(id=1)
    amount = float(request.GET.get('amount', 0))
    price = get_doge_price()

    if wallet.doge >= amount:
        wallet.balance_usdt += amount * price
        wallet.doge -= amount
        wallet.save()

    return JsonResponse({'status': 'ok'})