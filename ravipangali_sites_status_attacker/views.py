from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ravipangali_sites_status_attacker.models import SiteStatus


@api_view(['POST'])
def change_site_status(request):
    if request.data['code'] == 'livi':
        status_value = request.data['status']
        description = request.data['description']
        site_status = SiteStatus.objects.first()
        if site_status:
                site_status.status = status_value
                site_status.description = description
                site_status.save()
        else:
            site_status = SiteStatus.objects.create(
                status=status_value,
                description=description
            )
        return Response({'message': 'Site status changed successfully'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Access Denied'}, status=status.HTTP_400_BAD_REQUEST)
