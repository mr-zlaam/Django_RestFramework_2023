from rest_framework import serializers
from apis.models import *


# create Serilizers
class Company_serializers(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()

    class Meta:
        model = Company
        fields = "__all__"


class Employee_serializers(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = "__all__"
