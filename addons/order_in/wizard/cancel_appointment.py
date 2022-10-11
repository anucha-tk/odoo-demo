from odoo import models, fields


class CancelAppointment(models.TransientModel):
    _name = "cancel.appointment.wizard"
    _description = "Cancel Appointment Wizard"

    appointment_id = fields.Many2one("order.appointment", string="Appointment")
    reason = fields.Text(string="Reason")

    def action_cancel(self):
        return
