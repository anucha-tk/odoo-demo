from odoo import models, fields, api


class Tag(models.Model):
    _name = "tag"
    _description = "Tag"

    name = fields.Char("name")
    color = fields.Char("color", default="#000000")
