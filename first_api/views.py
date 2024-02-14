from rest_framework.views import APIView
from rest_framework.response import Response



class HelloApiView(APIView):
    
    def get(self, request, *args, **kwargs):
        return Response({'message': 'Hello, World!'})

    def post(self, request, *args, **kwargs):
        # print(request.data)
        # print(request.POST)
        name = request.data.get('name', None)
        return Response({'result': f"Salom! {name}"}, status=201)


