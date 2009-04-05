# from http://www.djangosnippets.org/snippets/342/ by miracle2k
def load_templatetags():
    from django.conf import settings
    from django.template import add_to_builtins
    # This is important: If the function is called early, and some of the custom
    # template tags use superclasses of django template tags, or otherwise cause
    # the following situation to happen, it is possible that circular imports 
    # cause problems: 
    # If any of those superclasses import django.template.loader (for example,
    # django.template.loader_tags does this), it will immediately try to register
    # some builtins, possibly including some of the superclasses the custom template
    # uses. This will then fail because the importing of the modules that contain 
    # those classes is already in progress (but not yet complete), which means that 
    # usually the module's register object does not yet exist.
    # In other words:
    #       {custom-templatetag-module} ->
    #       {django-templatetag-module} ->
    #       django.template.loader ->
    #           add_to_builtins(django-templatetag-module)
    #           <-- django-templatetag-module.register does not yet exist
    # It is therefor imperative that django.template.loader gets imported *before*
    # any of the templatetags it registers.
    import django.template.loader

    try:
        for lib in settings.TEMPLATE_TAGS:
            add_to_builtins(lib)
    except AttributeError:
        pass