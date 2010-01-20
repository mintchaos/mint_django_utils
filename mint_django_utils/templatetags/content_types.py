from django import template
from django.template.loader import render_to_string

register = template.Library()

class RenderTemplateForNode(template.Node):
    def __init__(self, object, template_dir):
        self.object = object
        self.template_dir = template_dir.rstrip('/')
    def render(self, context):
        try:
            obj = template.resolve_variable(self.object, context)
            ctype_str = '%s.%s' % (obj._meta.app_label, obj._meta.module_name)
            context.push()
            context['object'] = obj
            template_list = []
            if ',' in self.template_dir:
                for tdir in self.template_dir.split(','):
                    template_list.append('%s/%s.html' % (tdir, ctype_str))
                    template_list.append('%s/default.html' % tdir)
            else:
                template_list.append('%s/%s.html' % (self.template_dir, ctype_str))
                template_list.append('%s/default.html' % self.template_dir)

            output = render_to_string(template_list, context)
            context.pop()
            return output
        except template.VariableDoesNotExist:
            return ''


@register.tag()
def render_template_for(parser, token):
    """
    Renders a template matching the app_name.module_name of the given object
    in the given template directory, falling back to default.html.

    If called as ``{% render_template_for story_object in "includes/story_list_snippets" %}``
    it would first look for includes/story_list_snippets/news.stories.html and then
    for includes/story_list_snippets/default.html.

    This is particularly useful when dealing with object of unknown type as
    it keeps nasty nested {% if %} blocks out and allows you to customize where desired.

    The object passed to the tag will be available in the rendered template
    as ``object``. The current context is also made available.

    """
    try:
        tag_name, object, in_var, template_dir = token.contents.split()
    except ValueEerror:
        raise template.TemplateSyntaxError, "%s tag requires three arguments '[object] in [template_dir]'" % token.contents.split()[0]
    if in_var != 'in':
        raise template.TemplateSyntaxError, "%s tag's second argument must be the keyword 'in'" % tag_name
    if template_dir[0] != template_dir[-1] or template_dir[0] not in ('"', "'"):
        raise template.TemplateSyntaxError, "%s tag's final argument should be in quotes" % tag_name
    return RenderTemplateForNode(object, template_dir[1:-1])

