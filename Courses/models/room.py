from odoo import fields, models,exceptions,api

class Room(models.Model):
    _name = 'courses.room'
    name=fields.Char(string="Name")
    capacity=fields.Integer(string="Capacity")
    sequence=fields.Char(string="Sequence")


    @api.constrains('capacity')
    def _check_value(self):
        if self.capacity > 50 or self.capacity < 0:
            raise exceptions.ValidationError(('Enter Value Between 0-50.'))