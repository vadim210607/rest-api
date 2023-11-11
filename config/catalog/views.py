from django.contrib.auth.models import User
from django.shortcuts import render  # тут походу не нада

from catalog.models import Perfum, Brand, Bottle
from catalog.serializers import PerfumSerializer, BottleSerializer, UserListAPISerializer

from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from rest_framework.decorators import action

from rest_framework.permissions import IsAdminUser

from rest_framework.pagination import PageNumberPagination


class BottleView(mixins.ListModelMixin,
                 mixins.UpdateModelMixin,
                 GenericViewSet):
    queryset = Bottle.objects.all()
    serializer_class = BottleSerializer
    permission_classes = [IsAdminUser]


class UserListAPI(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListAPISerializer


class PerfumViewSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 6


# class PerfumViewSet(viewsets.ModelViewSet): # Знизу імпортовано адресно та ролзширено
class PerfumViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    serializer_class = PerfumSerializer

    pagination_class = PerfumViewSetPagination

    queryset = Perfum.objects.all()  # Розшируємо через функцію знизу

    # # Функція Можна без неї, але виводе всі
    # def get_queryset(self):
    #     pk = self.kwargs.get('pk')
    #     if not pk:
    #         return Perfum.objects.all()
    #     return Perfum.objects.filter(pk=pk)

    @action(methods=['get'], detail=False)
    def brand_list(self, request):
        brand_list_all = Brand.objects.all()
        return Response({'brand_list': [i.name for i in brand_list_all]})

    @action(methods=['get'], detail=True)
    def brand(self, request, pk=None):
        brand_item_get = Brand.objects.get(pk=pk)
        return Response({'brand_item': brand_item_get.name})



# Представлення на основі Generic Class-Based
# class PerfumAPIList(generics.ListCreateAPIView):
#     queryset = Perfum.objects.all()
#     serializer_class = PerfumSerializer
#
# class PerfumAPIUpdate(generics.UpdateAPIView):
#     queryset = Perfum.objects.all()
#     serializer_class = PerfumSerializer
#
# class PerfumAPIGRUD(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Perfum.objects.all()
#     serializer_class = PerfumSerializer


# === Представлення на основі класу APIView ===
# class PerfumAPI(APIView):
#
#     def get(self, request):
#         perfum_list_all = Perfum.objects.all()
#         return Response({'perfum_list_all': PerfumSerializer(perfum_list_all, many=True).data})
#
#     def post(self, request):
#         serializer = PerfumSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save() # після добавки CREATE
#
#         return Response({'perfum_new_create': serializer.data})
#
#         # Добавив в класі серіалізатора функцію CREATE
#         # perfum_new = Perfum.objects.create(
#         #     title=request.data['title'],
#         #     content=request.data['content'],
#         #     brand_id=request.data['brand_id'],
#         #     bottle_id=request.data['bottle_id']
#         # )
#         # return Response({'perfum_new_create': PerfumSerializer(perfum_new).data})
#
#     def put(self, request, *args, **kwargs):
#         post_id = kwargs.get('pk', None)
#         if not post_id:
#             return Response({'error': 'Метод PUT не дозволений'})
#
#         try:
#             instance = Perfum.objects.get(pk=post_id)
#         except:
#             return Response({'error': 'Обєкт не існує'})
#
#         serializer = PerfumSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'perfum_update': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         post_id = kwargs.get('pk', None)
#         if not post_id:
#             return Response({'error': 'Метод DELETE не дозволений'})
#
#         # Код для видалення поста
#
#         return Response({'perfum_delete': 'Вдало видалено пост №' +str(pk)})


# https://www.django-rest-framework.org/tutorial/3-class-based-views/





