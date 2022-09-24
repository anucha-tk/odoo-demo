# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    "name": "Order In",
    "version": "1.0.0",
    "author": "anucha.tk",
    "sequence": -100,
    "category": "Order",
    "summary": "Order In management system",
    "description": """Order In management system""",
    "depends": [],
    "data": [
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/customer_view.xml",
    ],
    "demo": [],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
