# -*- coding: utf-8 -*-
from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    # Add a new column to the res.partner model, by default partners are not
    # instructors
    instructor = fields.Boolean("Instructor", default=False)
    # why it is only for attendees, not for instructor?!
    session_ids = fields.Many2many('openacademy.session',
        string="Attended Sessions", readonly=True)
    teached_ids = fields.One2many(
        string="Lectured Sessions",
        comodel_name="openacademy.session",
        help="Lectured session",
        readonly=True)
