from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class exportarApiView(APIView):
    
    permission_classes = [AllowAny]

    def get(self, request):

        
        return Response('Ok')
    
    def post(self, request):
        pdf_file = request.FILES['files']
        print(pdf_file)
        
        return Response('Ok')