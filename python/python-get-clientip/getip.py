from django.http.response import JsonResponse

def get_client_ip(request):
    """
    A method to get the cient ip address.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        ip = request.META.get('REMOTE_ADDR')

    # if you want add range /24 to the rule:
    # s = ip.split(".")
    # ip = "{}.{}.{}.0/24".format(s[0], s[1], s[2])
    return ip 

def s2ptestview(request):
    ip = get_client_ip(request)
    resp = {"status": 200, "info": "Your ip address is " + ip}
    return JsonResponse(resp)

if __name__ == "__main__":
  s2ptestview(request)