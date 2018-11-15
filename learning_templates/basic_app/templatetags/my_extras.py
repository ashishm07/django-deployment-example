from django import template


# How to make your own template filter
register = template.Library()

def cut(value,arg):

    """
    This cuts out all balues of arg from the string
    """

    return value.replace(arg,'')

register.filter('cut',cut)
