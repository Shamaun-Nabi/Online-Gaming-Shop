from django import template

register=template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product  , cart):
    keys = cart.keys()
    for id in keys:
        # print(id,cart)
        if int(id)== product.id:
            return True
    return False


@register.filter(name='cart_quantity')
def cart_quantity(product  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0

@register.filter(name='price_total')
def price_total(product  , cart):
    return product.price * cart_quantity(product , cart)


@register.filter(name='total_cart_price')
def total_cart_price(product , cart):
    sum = 0 
    for p in product:
        sum += price_total(p , cart)
    return sum

@register.filter(name='custom_sign')
def custom_sign(product  , cart):
    return ("৳")
@register.filter(name='multiply')
def multiply(number,number1):
    return number*number1
