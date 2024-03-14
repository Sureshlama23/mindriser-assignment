from django.shortcuts import render


class underConstructionMiddleware:

  def __init__(self,get_response):
    self.get_response = get_response

  def __call__(self,request):
    response = render(request,'blog/siteuc.html')
    return response