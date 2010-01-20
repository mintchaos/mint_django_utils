from django.shortcuts import render_to_response as django_render_to_response
from django.template import RequestContext

def render_to_response(req, *args, **kwargs):
    kwargs['context_instance'] = RequestContext(req)
    return django_render_to_response(*args, **kwargs)