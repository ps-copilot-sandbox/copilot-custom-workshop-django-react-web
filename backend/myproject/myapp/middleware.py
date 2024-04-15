from django.utils.deprecation import MiddlewareMixin

class CorsMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Headers"] = "content-type"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"  # Add this line
        return response