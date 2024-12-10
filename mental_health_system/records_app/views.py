from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Order, OrderItem, Product
from .serializers import CustomerSerializer, OrderSerializer, OrderItemSerializer, ProductSerializer

# Healthcare Providers: Access and update patient records
class PatientRecordsView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Patients: Access own mental health records
class PatientView(APIView):
    def get(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        except Customer.DoesNotExist:
            return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)