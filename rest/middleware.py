from django.http.response import HttpResponseForbidden

# middleware as func
def blacklist_middleware(get_response): # django define get_response
    def middleware(request):
        client_ip = get_client_ip(request)
        if client_ip in blacklist:
            return HttpResponseForbidden()

        response = get_response(request)
        return response

    return middleware


# middleware as class
class BlacklistMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response # django define get_response

    def __call__(self, request):
        client_ip = get_client_ip(request)
        if client_ip in blacklist:
            return HttpResponseForbidden

        response = self.get_response(request)
        return response

# now we should add them in MIDDLEWARE in settings.