

class CustomMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("adding a log")
        response = self.get_response(request)

        response['custom-header'] = "abc"
        return response
