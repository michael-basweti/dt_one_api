from attr import fields
from rest_framework import serializers
from .models import Loans, Payavenue, Paymenttype, Payments, Vwloans, Vwunpaidloans


class LoansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loans
        fields = '__all__'


class PayavenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payavenue
        fields = '__all__'


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paymenttype
        fields = '__all__'

class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class VwLoansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vwloans
        fields = '__all__'


class VwUnpaidLoansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vwunpaidloans
        fields = '__all__'