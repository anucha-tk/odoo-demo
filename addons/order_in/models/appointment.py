from odoo import models, fields, api


class OrderAppointment(models.Model):
    _name = "order.appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Order Appointment"
    _rec_name = "customer_id"

    customer_id = fields.Many2one("order.customer", string="Customer", required=True)
    appointment_time = fields.Datetime(string="Appointment Time", required=True, default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", required=True, default=fields.Date.context_today)
    types = fields.Selection(
        string="customer_type",
        related="customer_id.types",
    )
    ref = fields.Char(string="Reference", tracking=True)

    @api.onchange("customer_id")
    def _onchange_customer_id(self):
        self.ref = self.customer_id.ref
