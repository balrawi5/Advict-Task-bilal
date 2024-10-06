{
    'name': 'Task',
    'author': 'Bilal Alrawi',
    'sequence': 1,
    'Technical Name': 'Advict_Task',
    'depends': ['sale_management', 'account', 'product'],
    'data': [
                'views/product.xml',
                'views/sales_order.xml',
                'views/account_move.xml',
                'data/sequence.xml',
                'views/menu.xml',
                'security/ir.model.access.csv',
            ],

    'installable': True,
    'application': True,

}