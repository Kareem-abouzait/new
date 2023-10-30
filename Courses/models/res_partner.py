from odoo import fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"
    
    name=fields.Char(string="Name")
    is_instructor=fields.Boolean(string="Is Instructor")
    course=fields.Many2one('courses.course',string="Course")
    course_id=fields.Many2one('courses.course', string='Course Id',)
