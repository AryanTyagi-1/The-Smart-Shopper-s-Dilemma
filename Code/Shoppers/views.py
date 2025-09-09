from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from asgiref.sync import sync_to_async
import asyncio
from .scraper import fetch_products

@csrf_exempt
@cache_page(60 * 10)  
async def product_search(request):
    query = request.GET.get('query', '')
    if not query:
        return JsonResponse({'error': 'Missing query'}, status=400)
    result = await fetch_products(query)
    return JsonResponse({'results': result})
