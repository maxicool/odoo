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
    # for one2many inverse_name is obliged
    instructor_ids = fields.One2many(
        string="Lectured Sessions",
        comodel_name="openacademy.session",
        inverse_name="instructor_id",
        help="Lectured session",
        readonly=True)

# new_field_ids = fields.Many2many(
#     string="Field name",
#     comodel_name="res.partner",
#     relation="relation_table_name",
#     column1="column_this",
#     column2="column_other",
#     domain="[('field', '=', other)]",
#     context={"key": "value"},
#     help="Explain your field.",
# )
# new_field_ids = fields.One2many(
#     string="Field name",
#     comodel_name="res.partner",
#     inverse_name="inverse_name_id",
#     domain="[('field', '=', other)]",
#     context={"key": "value"},
#     help="Explain your field.",
# )
