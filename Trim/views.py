import os
import json
from django.http import JsonResponse
from gptrim import trim

api_key = os.environ['API_KEY']

def Home(request):
    if request.method == 'POST':
        api_key_in_header = request.META.get('HTTP_API_KEY')

        if api_key_in_header != api_key:
            return JsonResponse({ 'message': 'Required correct API key', 'success': False})
        
        body = json.loads(request.body)

        text = body.get('text')
        
        trimmed_text = trim(text)

        return JsonResponse({ 'trimmed_text': trimmed_text, 'success': True })
    else:
        return JsonResponse({"message": 'Only POST method acceptable', 'success': False })

