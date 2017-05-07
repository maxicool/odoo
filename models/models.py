# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string="Title", required=True)

    #string has no effect by upgrade, but works after reinstall again
    #description = fields.Text(string="what is up"
    description = fields.Text()

    # add a responsible person for the Course,
    # since the responsible must be in the organization, there is a link to
    # res.users
    responsible = fields.Many2one(
        string="Responsible",
        comodel_name="res.users",
        #domain="[('field', '=', other)]",
        #context={"key": "value"},
        ondelete="set null",
        index=True,
        help="Person who in charge for the course",
    )

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
# restarting odoo, model can be updated after upgrading app
class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    # digits=(6, 2) specifies the precision of a float number: 6 is the total
    # number of digits, while 2 is the number of digits after the comma. Note
    # that it results in the number digits before the comma is a maximum 4
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")

    # add instructors and session related course.
    # a session is only related to one course, but a course may open many sessions
    # a session has one instructor, and a instructor may give lessons to a lot of session
    # and instructors are in res.partner
    instructor_id = fields.Many2one('res.partner', string="Instructor",
        domain=['|', ('instructor','=',True),
                    ('category_id.name', 'ilike', 'teacher')])
    course_id = fields.Many2one('openacademy.course',
        ondelete='cascade', string="Course", required=True)
    # a Many2many relation, attendees can take part in many sessions,
    # while a session can have a lot of attendees
    attendee_ids = fields.Many2many(
        string="Attendees",
        comodel_name="res.partner",
        help="students who coming for the session",
    )

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
