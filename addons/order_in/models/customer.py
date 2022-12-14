from datetime import date
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


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
    appointment_count = fields.Integer(compute="_compute_appointment_count", string="Appointment Count", store=True)
    appointment_ids = fields.One2many("order.appointment", "customer_id", string="Appointments")
    parent = fields.Char("Parent")

    @api.depends("appointment_ids")
    def _compute_appointment_count(self):
        for rec in self:
            rec.appointment_count = self.env["order.appointment"].search_count([("customer_id", "=", rec.id)])

    @api.constrains("date_of_birth")
    def _constrains_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > fields.Date.today():
                raise ValidationError(_("The entered date of birth is not acceptable !"))

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

    def name_get(self):
        return [(record.id, "[%s] %s" % (record.ref, record.name)) for record in self]
