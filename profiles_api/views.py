from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test api view"""

    def get(self, request, format = None):
        """Returns a list of apiview features"""
        an_apiview =[
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a tradtional Django View',
            'gives you the most control over you application logic',
            'is mapped manually to URLs'
        ]

        return Response({'message':'hello!','an_apiview': an_apiview})
