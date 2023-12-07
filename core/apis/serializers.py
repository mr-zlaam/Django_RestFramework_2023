from rest_framework import serializers
from apis.models import *


# create Serilizers
class Company_serializers(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()

    class Meta:
        model = Company
        fields = "__all__"
