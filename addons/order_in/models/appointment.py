from odoo import models, fields, api


class OrderAppointment(models.Model):
    _name = "order.appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Order Appointment"

    customer_id = fields.Many2one("order.customer", string="Customer", required=True)
    appointment_time = fields.Datetime(string="Appointment Time", required=True)
    booking_date = fields.Date(string="Booking Date", required=True)
