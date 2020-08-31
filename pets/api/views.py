from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication

from ..models import Pet
from ..serializers import PetSerializer, PetListSerializer

@api_view(['GET'])
def pet_detail_api_view(request, id, *args, **kwargs):
    qs = Pet.objects.filter(id=id)
    if not qs.exists():
        return Response({"detail": "Pet not found"}, status=404)
    profile_obj = qs.first()
    serializer = PetSerializer(instance=profile_obj, context={"request": request})
    return Response(serializer.data, status=200)

@api_view(['GET'])
def pet_list_api_view(request, username, *args, **kwargs):
    qs = Pet.objects.filter(user__username=username)

    
    
    serializer = PetListSerializer(instance=qs, many=True)
    return Response(serializer.data, status=200)