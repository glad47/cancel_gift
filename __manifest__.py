{
    'name': 'Gift Card Cancellation',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Cancel gift cards by setting points to 0',
    'description': """
        This module allows users to cancel gift cards by entering the gift card code
        and setting the points balance to 0.
    """,
    'depends': ['base', 'sale'],
    'data': [
        'security/gift_card_security.xml',
        'security/ir.model.access.csv',
        'views/gift_card_cancel_view.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}