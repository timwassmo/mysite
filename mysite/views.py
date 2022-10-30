from .models import Car, Customer, Order
from rest_framework.response import Response
from .serializers import CarSerializer, CustomerSerializer, OrderSerializer
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_cars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_customers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def save_car(request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)




@api_view(['PUT'])
def update_car(request, id):
    try:
        the_car = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CarSerializer(the_car, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_car(request, id):
    try:
        the_car = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    the_car.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])

def order_car(request, car_id, customer_id):
    """Creates order with key for Customer and Car. 
    Edits customer order status and car availability"""
    
    order_serializer = OrderSerializer(data={"car": car_id, "customer": customer_id})
    if order_serializer.is_valid():
        try:
            the_car = Car.objects.get(pk=car_id)
            the_customer = Customer.objects.get(pk=customer_id)
            
        except Car.DoesNotExist or Customer.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if the_car.status != "booked" :
            Car.objects.filter(pk=car_id).update(status='booked')
            if the_customer.active_order == False:
                Customer.objects.filter(pk=customer_id).update(active_order=True)
                order_serializer.save()
                return Response(order_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response("Customer has booking registered", status=status.HTTP_403_FORBIDDEN)
        else:
            return Response("Car already booked", status=status.HTTP_403_FORBIDDEN)
        
            
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view([''])
def cancel_ordered_car(id):
    pass


@api_view([''])
def rent_car(id):
    pass


@api_view([''])
def return_car(id):
    pass
