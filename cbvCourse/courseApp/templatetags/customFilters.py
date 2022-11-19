from django import template
register = template.Library()


def custLower(value):
    result = value[::3].lower()
    return result


register.filter("myLower", custLower)
