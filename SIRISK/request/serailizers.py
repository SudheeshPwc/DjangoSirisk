from rest_framework.serializers import ModelSerializer
from request.models import  TransRequest,TransResponse

class TransRequestSerailizer(ModelSerializer):
    class Meta:
        model=TransRequest
        fields='__all__'

class TransResponseSerailizer(ModelSerializer):
    class Meta:
        model=TransResponse
        fields='__all__'