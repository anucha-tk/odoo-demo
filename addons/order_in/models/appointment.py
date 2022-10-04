from email.policy import default
from odoo import models, fields, api


class OrderAppointment(models.Model):
    _name = "order.appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Order Appointment"

    customer_id = fields.Many2one("order.customer", string="Customer", required=True)
    appointment_time = fields.Datetime(string="Appointment Time", required=True, default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", required=True, default=fields.Date.context_today)
