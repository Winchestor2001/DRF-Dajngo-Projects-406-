from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class HelloApiView(APIView):
    
    def get(self, request, *args, **kwargs):
        return Response({'message': 'Hello, World!'})

    def post(self, request, *args, **kwargs):
        # print(request.data)
        # print(request.POST)
        name = request.data.get('name', None)
        return Response({'result': f"Salom! {name}"}, status=201)


class FruitsAPIView(APIView):
    fruits = ['Qizil Olma', 'Sariq olma', 'Yashil olma', 'Chirigan olma', 'Olmaga oxshagan nok']
    
    def get(self, request, *args, **kwargs):
        return Response({"fruits": self.fruits}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        fruit_name = request.data.get('fruit_name')
        self.fruits.append(fruit_name)
        return Response({"fruits": self.fruits}, status=status.HTTP_201_CREATED)
    
    def put(self, request, *args, **kwargs):
        fruit_index = int(request.data.get('index'))
        new_fruit = request.data.get('new_fruit')

        if len(self.fruits) > fruit_index:
            self.fruits[fruit_index] = new_fruit
            return Response({"fruits": self.fruits}, status=status.HTTP_205_RESET_CONTENT)

        else:
            return Response({"error": "index xato"}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request):
        fruit_index = int(request.data.get('index'))
        if len(self.fruits) > fruit_index:
            self.fruits.pop(fruit_index)
            return Response({"fruits": self.fruits}, status=status.HTTP_204_NO_CONTENT)

