from django.shortcuts import render
from django.http import HttpResponse
from .models import SiteStatus

class SiteStatusMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip admin, static, and media file requests
        if (request.path.startswith('/admin/') or 
            request.path.startswith('/static/') or 
            request.path.startswith('/media/')):
            return self.get_response(request)
        
        try:
            # Get the first SiteStatus record
            site_status = SiteStatus.objects.first()
            
            # If no SiteStatus record exists or status is False, show maintenance page
            if not site_status or not site_status.status:
                # Skip if already on the site status page to avoid infinite redirect
                if 'site_status' in request.path:
                    return self.get_response(request)
                
                # Render the site status template
                context = {
                    'status_message': site_status.description if site_status else 'Site is currently under maintenance.'
                }
                return render(request, 'layouts/site_status.html', context)
                
        except Exception:
            # If there's any error accessing the database, allow the request to proceed
            pass
        
        # If status is True or any error occurred, proceed with normal request
        response = self.get_response(request)
        return response