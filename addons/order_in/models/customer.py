from datetime import date
from odoo import models, fields, api


class OrderCustomer(models.Model):
    _name = "order.customer"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Customer"

    name = fields.Char(string="Name", required=True, tracking=True)
    date_of_birth = fields.Date(string="Date Of Birth")
    age = fields.Integer(string="Age", compute="_compute_age", tracking=True)
    address = fields.Char(string="Address", required=True, tracking=True)
    phone = fields.Char(string="Phone", required=True, tracking=True)
    email = fields.Char(string="Email", required=True, tracking=True)
    ref = fields.Char(string="Reference", tracking=True)
    active = fields.Boolean(string="Active", default=True)
    types = fields.Selection(
        [
            ("clinic", "Clinic"),
            ("hospital", "Hospital"),
            ("other", "Other"),
        ],
        string="customer_type",
    )
    tag_ids = fields.Many2many("tag", string="tags")
    image = fields.Image("Image")

    @api.model
    def create(self, vals):
        vals["ref"] = self.env["ir.sequence"].next_by_code("customer")
        return super(OrderCustomer, self).create(vals)

    def write(self, vals):
        if not self.ref and not vals.get("ref"):
            vals["ref"] = self.env["ir.sequence"].next_by_code("customer")
        return super(OrderCustomer, self).write(vals)

    @api.depends("date_of_birth")
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0
