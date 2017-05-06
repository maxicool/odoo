# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string="Title", required=True)

    #string has no effect by upgrade, but works after reinstall again
    #description = fields.Text(string="what is up"
    description = fields.Text()

'''
Create a session model
For the module Open Academy, we consider a model for sessions: a session is an
occurrence of a course taught at a given time for a given audience.

Create a model for sessions. A session has a name, a start date, a duration and
a number of seats. Add an action and a menu item to display them. Make the new
model visible via a menu item.

Create the class Session in openacademy/models/models.py.
Add access to the session object in openacademy/view/openacademy.xml.
'''

# We check if we can use upgrade app, to update models
class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")

# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
