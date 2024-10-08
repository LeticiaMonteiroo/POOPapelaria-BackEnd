# from django.shortcuts import render

# def cadastro(request):
#     return render(request,'') #retorna o html do cadastro

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken

@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']

    _, token = AuthToken.objects.create(user)

    return Response({
        'user_info': {
            'id': user.id,
            'username': user.username,
            'email': user.email
            },
        'token': token
    })
