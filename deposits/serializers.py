from rest_framework import serializers
from deposits.models import Deposit

class DepositSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deposit
        fields = '__all__'