import unittest
from django.template import Library
from django.template.defaultfilters import lower

register = Library()

@register.filter
def gt(value, arg):
    "Returns a boolean of whether the value is greater than the argument"
    return value > int(arg)

@register.filter
def lt(value, arg):
    "Returns a boolean of whether the value is less than the argument"
    return value < int(arg)

@register.filter
def gte(value, arg):
    "Returns a boolean of whether the value is greater than or equal to the argument"
    return value >= int(arg)

@register.filter
def lte(value, arg):
    "Returns a boolean of whether the value is less than or equal to the argument"
    return value <= int(arg)

@register.filter
def length_gt(value, arg):
    "Returns a boolean of whether the value's length is greater than the argument"
    return len(value) > int(arg)

@register.filter
def length_lt(value, arg):
    "Returns a boolean of whether the value's length is less than the argument"
    return len(value) < int(arg)

@register.filter
def length_gte(value, arg):
    "Returns a boolean of whether the value's length is greater than or equal to the argument"
    return len(value) >= int(arg)

@register.filter
def length_lte(value, arg):
    "Returns a boolean of whether the value's length is less than or equal to the argument"
    return len(value) <= int(arg)

@register.filter
def is_content_type(obj, arg):
    ct = lower(obj._meta.object_name)
    return ct == arg

@register.filter
def is_equal(obj, arg):
    "Returns a boolean of whether the value is equal to the argument"
    return obj == arg

@register.filter
def round(obj):
    "Returns a number rounded."
    return round(obj)

@register.filter
def has(obj, arg):
    try:
        if arg in obj:
            return True
    except TypeError:
        pass
    return False

@register.filter
def is_empty(value):
    "Returns a boolean if the value passed has non whitespace"
    if not value.strip():
        return True
    else:
        return False

class ComparisonTestCase(unittest.TestCase):

    def test_is_empty_empty(self):
        self.assertEqual(True, is_empty(""))

    def test_is_empty_nl(self):
        self.assertEqual(True, is_empty("\n"))

    def test_is_empty_nls_and_spaces(self):
        self.assertEqual(True, is_empty("\n     	\n  "))

    def test_is_empty_a_letter(self):
        self.assertEqual(False, is_empty("\n     s	\n  "))

    def test_is_empty_less_letters(self):
        self.assertEqual(False, is_empty("\ns"))

    def test_is_empty_string(self):
        self.assertEqual(False, is_empty("s"))

if __name__ == '__main__':
    unittest.main()