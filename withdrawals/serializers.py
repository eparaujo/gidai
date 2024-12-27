from rest_framework import serializers
from withdrawals.models import Withdrawal

class WithdrawalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Withdrawal
        fields = '__all__'