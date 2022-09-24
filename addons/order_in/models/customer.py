from odoo import models, fields, api


class OrderCustomer(models.Model):
    _name = "order.customer"
    _description = "Customer"

    name = fields.Char(string="Name", required=True)
    address = fields.Char(string="Address", required=True)
    phone = fields.Char(string="Phone", required=True)
    email = fields.Char(string="Email", required=True)
