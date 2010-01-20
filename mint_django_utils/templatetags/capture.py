# my personal "fork" of http://www.djangosnippets.org/snippets/545/

from django import template

register = template.Library()

@register.tag(name='capture')
def do_captureas(parser, token):
    try:
        tag_name, _as, varname = token.contents.split()
    except ValueError:
        raise template.TemplateSyntaxError("'capture' requires a variable name.")
    nodelist = parser.parse(('endcapture',))
    parser.delete_first_token()
    return CaptureasNode(nodelist, varname)

class CaptureasNode(template.Node):
    def __init__(self, nodelist, varname):
        self.nodelist = nodelist
        self.varname = varname

    def render(self, context):
        output = self.nodelist.render(context)
        context[self.varname] = output
        return ''
