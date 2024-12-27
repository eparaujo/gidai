from rest_framework import serializers
from kindexpenses.models import KindExpense

class KindexpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = KindExpense
        fields = '__all__'