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
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_customers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    print(serializer.data)
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
    """Implement an endpoint ‘order-car’ where a customer-id, car-id is passed as parameters.
    The system must check that the customer with customer-id has not booked other cars. The
    system changes the status of the car with car-id from ‘available’ to ‘booked’."""
    
    order_serializer = OrderSerializer(data={"car": car_id, "customer": customer_id})
    
    if order_serializer.is_valid():
        try:
            the_car = Car.objects.get(pk=car_id)
            the_customer = Customer.objects.get(pk=customer_id)
            
        except Car.DoesNotExist or Customer.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)



        if the_car.status == "available" and the_customer.activer_order == False:
            order_serializer.save()
            the_customer.activer_order = True
            print(f'order_serializer: {order_serializer}')
            return Response(order_serializer.data, status=status.HTTP_201_CREATED)



@api_view([''])
def cancel_ordered_car(id):
    pass


@api_view([''])
def rent_car(id):
    pass


@api_view([''])
def return_car(id):
    pass
