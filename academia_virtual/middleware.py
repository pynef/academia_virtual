# -*- coding: utf-8 -*-
from django.http import JsonResponse, HttpResponse

class InfoMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.session['cursos'] = []
        return self.get_response(request)
