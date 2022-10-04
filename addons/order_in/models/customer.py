from odoo import models, fields, api


class OrderCustomer(models.Model):
    _name = "order.customer"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Customer"

    name = fields.Char(string="Name", required=True, tracking=True)
    address = fields.Char(string="Address", required=True, tracking=True)
    phone = fields.Char(string="Phone", required=True, tracking=True)
    email = fields.Char(string="Email", required=True, tracking=True)
    active = fields.Boolean(string="Active", default=True)
    types = fields.Selection(
        [
            ("clinic", "Clinic"),
            ("hospital", "Hospital"),
            ("other", "Other"),
        ],
        string="customer_type",
    )
