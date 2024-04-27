from rest_framework import serializers
from .models import Clogs


class Clogsserializer(serializers.ModelSerializer):
    customer_name = serializers.SerializerMethodField()

    class Meta:
        model = Clogs
        fields = [
            "customer_name",
            "customer",
            "imsi",
            "imei",
            "plan",
            "call_type",
            "corresp_type",
            "corresp_isdn",
            "duration",
            "time",
            "date"
        ]

    def get_customer_name(self, obj):
        if obj.customer:
            return obj.customer.name
        return None
