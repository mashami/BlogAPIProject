
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.parsers import JSONParser
from .models import Articles
from .serializers import ArticlesSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import generics
from rest_framework import mixins,viewsets

# Create your views here.


class GenericAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class=ArticlesSerializer
    queryset=Articles.objects.all()
    
    def get (self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
class GenericAPIViewDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class=ArticlesSerializer
    queryset=Articles.objects.all()
    lookup_field='id'
    
    def get (self,request, id=None):
        if id:
            return self.retrieve(request)
        else:
            
            return self.list(request)
    
    def put (self,request,id=None):
        return self.update(request, id)
    
    
    def delete(self,request,id=None):
        return self.destroy(request,id)
    
#==========================================================================================================================
# class ArticleAPIView(APIView):
#     def get(self,request):
#         article=Articles.objects.all()
#         serializer=ArticlesSerializer(article, many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer=ArticlesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class Details(APIView):
#     def get_object(self,id):
#         try:
#            return Articles.objects.get(id=id)
#         except Articles.DoesNotExist:
#            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
       
#     def get(self,request,id):
#         article=self.get_object(id)
#         serializer=ArticlesSerializer(article)
#         return Response(serializer.data)
    
    
#     def put(self,request,id):
#         article=self.get_object(id)
#         serializer=ArticlesSerializer(article,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

#     def delete(self,request,id):
#         article=self.get_object(id)
#         article.delete()
        
#         return Response(status=status.HTTP_204_NO_CONTENT)

    

# ===========================================================================================================

# @api_view(['GET','POST'])
# def Articles_list(request):
#     if request.method=='GET':
#         article=Articles.objects.all()
#         serializer=ArticlesSerializer(article, many=True)
#         return Response(serializer.data)
    
#     elif request.method=='POST':
        
#         serializer=ArticlesSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
# def Articles_list(request):
#     if request.method=='GET':
#         article=Articles.objects.all()
#         serializer=ArticlesSerializer(article, many=True)
#         return JsonResponse(serializer.data,safe=False)
    
#     elif request.method=='POST':
#         Data=JSONParser().parse(request)
#         serializer=ArticlesSerializer(data=Data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
        
#         return JsonResponse(serializer.errors, status=404)




   
    
    
    
# @api_view(['GET','PUT','DELETE'])
# def Article_details(request,pk):
#     try:
#         article=Articles.objects.get(pk=pk)
#     except Articles.DoesNotExist:
#         return Response(status=status.HTTP_400_BAD_REQUEST)
        
#     if request.method=='GET':
#         serializer=ArticlesSerializer(article)
#         return Response(serializer.data)
    
#     elif request.method=='PUT':
        
#         serializer=ArticlesSerializer(article,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
#     elif request.method=='DELETE':
#         article.delete()
#         print("deleted")
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
        
        


# @csrf_exempt
# def Article_details(request,pk):
#     try:
#         article=Articles.objects.get(pk=pk)
#     except Articles.DoesNotExist:
#         return HttpResponse(status=404)
        
#     if request.method=='GET':
#         serializer=ArticlesSerializer(article)
#         return JsonResponse(serializer.data)
    
#     elif request.method=='PUT':
#         data= JSONParser().parse(request)
#         serializer=ArticlesSerializer(article,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors,status=400)
    
    
#     elif request.method=='DELETE':
#         article.delete()
#         print("deleted")
#         return HttpResponse(status=204)
    
        
        
    

    