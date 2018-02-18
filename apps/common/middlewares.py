from django.utils.deprecation import MiddlewareMixin


class CorsMiddleWare(MiddlewareMixin):

  def process_request(self, request):
    pass

  def process_response(self, request, response):

    response['Access-Control-Allow-Origin'] = '*' # For now it's a wildcard.
    response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, Host, X-Date'
    return response
