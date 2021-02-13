from apps.base.api import GeneralListAPIView
from apps.payments.api.serializers.payment_serializers import PaySerializer

class PayListAPIView(GeneralListAPIView):
    serializer_class = PaySerializer