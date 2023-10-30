from odoo import fields, models,exceptions,api

class Course(models.Model):
    _name = 'courses.course'

    name = fields.Char(string="Name")
    instructor = fields.Many2one('res.partner',string="Instructor")
    room=fields.Many2one('courses.room',string="Room")
    attendees=fields.Many2many('res.partner',string="Attendees")

    @api.constrains('attendees')
    def _check_attendees(self):
        for rec in self:
            if len(rec.attendees) > rec.room.capacity:
                raise exceptions.ValidationError('Not more than Room Capacity :'+str(rec.room.capacity))