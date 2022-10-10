from odoo import models, fields, api


class Tag(models.Model):
    _name = "tag"
    _description = "Tag"

    name = fields.Char("Name")
    color = fields.Integer("Color")
