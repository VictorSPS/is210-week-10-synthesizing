#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""correlating two related data sets"""


def sum_orders(customers, orders):
    """Function takes two parameters customers and orders.
    Arg:
       customers(dict): A dictionary of customers keyed by customer_id.
       orders(dict): A dictionary of orders keyed by order id.
    Return:
       returns the combined dictionary.
    Examples:
       >>> CUSTOMERS = {2: {'name': 'Person One', 'email': 'email@one.com'},
                    3: {'name': 'Person Two', 'email': 'email@two.com'}}
       >>> ORDERS = {1: {'customer_id': 2, 'total': 10},
                 3: {'customer_id': 2, 'total': 10},
                 4: {'customer_id': 3, 'total': 15}}
       >>> sum_orders(customers=CUSTOMERS, orders=ORDERS)
       {2: {'email': 'email@one.com',
            'total': 20, 'orders': 2, 'name': 'Person One'},
       3: {'email': 'email@two.com',
           'total': 15, 'orders': 1, 'name': 'Person Two'}}
    """
    new_dict = {}
    orders = orders.values()
    for order in orders:
        key = order['customer_id']
        val1 = customers[key]['name']
        val2 = customers[key]['email']
        if key not in new_dict.iterkeys():
            val3 = 1
            val4 = order['total']
        else:
            val3 = new_dict[key]['orders'] + 1
            val4 = new_dict[key]['total'] + order['total']
        neworder = dict(name=val1, email=val2, orders=val3, total=val4)
        order_customer = {key: neworder}
        new_dict.update(order_customer)
    return new_dict
