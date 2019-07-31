from django import template

register = template.Library()


@register.simple_tag()
def multiply(operand1, operand2, *args, **kwargs):
    # you would need to do any localization of the result here
    return operand1 * operand2
