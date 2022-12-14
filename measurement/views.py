from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer, SensorSerializer


class ListCreateSensors(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    
    
class RetrieveUpdateSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects
    serializer_class = SensorDetailSerializer
    

class CreateMeasurement(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    
# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
