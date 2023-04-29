from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

# Create your views here.

def index(request):
    return render(request, 'chatbot/index.html')

#@api_view(['POST'])
@csrf_exempt
def executeMessage(request):
    if request.method == 'POST':
        print('Solicitação POST recebida!')
        return Response({'mensagem': 'Dados recebidos com sucesso.'})
    else:
        return Response({'mensagem': 'Metodo diferente de POST'})