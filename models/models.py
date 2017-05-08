# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

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

    # There is an session_ids in partner.py too!
    # session_ids = fields.Many2many('openacademy.session',
    #     string="Attended Sessions", readonly=True)
    # How to distinguish in xml ? by definition in
    # <field name="model">openacademy.course</field>
    session_ids = fields.One2many(
        string="Sessions",
        comodel_name="openacademy.session",
        inverse_name="course_id",
        help="fill sessions",
    )

    # add a new copy function, because of sql unique constraints
    # could be still errors:
    # copy of copy of (1)
    # copy of copy of (2)
    # then delet (1) and copy : copy of copy of 
    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u"Copy of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(Course, self).copy(default)

    # sql constraints
    # CHECK that the course description and the course title are different
    # Make the Course's name UNIQUE
    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]


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
    start_date = fields.Date(default=fields.Date.today)
    # digits=(6, 2) specifies the precision of a float number: 6 is the total
    # number of digits, while 2 is the number of digits after the comma. Note
    # that it results in the number digits before the comma is a maximum 4
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    # Add a field active in the class Session, and set sessions as active by default.
    active = fields.Boolean(default=True)

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

    taken_seats = fields.Float(
        string="Taken Seats",
        compute='_taken_seats')

    # Dependencies
    @api.depends("seats", "attendee_ids", )
    # definition of compute field _taken_seats
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                # the percentage of
                r.taken_seats = 100.0 * len(r.attendee_ids) /r.seats

    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': "The number of available seats may not be negative",
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': "Too many attendees",
                    'message': "Increase seats or remove excess attendees",
                },
            }

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.attendee_ids:
                raise exceptions.ValidationError("A session's instructor can't be an attendee")
