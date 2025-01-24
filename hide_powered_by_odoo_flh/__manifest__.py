{
    "name": "Hide Powered by Odoo",
    "summary": "Hide Powered by Odoo in Login, Website and POS",
    "version": "15.0.1.0.0",
    "category": "Extra Tools",
    "author": "WaiYan-DEVJ@K3R, FourLeafHouse",
    "license": "LGPL-3",
    "depends": ['base','web','portal','point_of_sale'],
    "data": [
        'views/portal_templates.xml',
        'views/webclient_templates.xml'
        ],
    'assets': {
        'web.assets_frontend': [
            'hide_powered_by_odoo/static/src/css/website.css',
        ],
        'point_of_sale._assets_pos': [
            'hide_powered_by_odoo/static/src/xml/order_receipt.xml',
        ],
    },
    "images": ['static/description/banner.png'],
    "application": True,
    "installable": True,
    "auto_install": False
}