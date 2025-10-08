import time


class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"[Middleware] request path: {request.path}")
        response = self.get_response(request)
        print(f"[Middleware] response path: {response.status_code}")
        return response


class TimerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        duration = time.time() - start
        print(f"[Middleware] response time: {duration:.2f} seconds")
        return response


class IpResolverMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        ip = request.META.get("REMOTE_ADDR")
        print(f"[Middleware] ip: {ip}")
        return self.get_response(request)
