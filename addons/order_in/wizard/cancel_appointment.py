import datetime
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CancelAppointment(models.TransientModel):
    _name = "cancel.appointment.wizard"
    _description = "Cancel Appointment Wizard"

    appointment_id = fields.Many2one("order.appointment", string="Appointment", domain=[("state", "=", "draft")])
    reason = fields.Text(string="Reason")
    date_cancel = fields.Date(string="Cancellation Date")

    def action_cancel(self):
        if self.date_cancel == fields.Date.today():
            raise ValidationError("cancellation isn't allow in the same day of booking")
        return

    @api.model
    def default_get(self, fields):
        res = super(CancelAppointment, self).default_get(fields)
        res["date_cancel"] = datetime.date.today()
        res["appointment_id"] = self.env.context.get("active_id")
        return res
