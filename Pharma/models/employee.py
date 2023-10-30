from odoo import fields, models

class Employee(models.Model):
    _name = 'pharma.employee'

    pharmacy_id = fields.Many2one('pharma.pharmacy', string="Pharmacy")
    name = fields.Char(string="Name")
    contact_info = fields.Text(string="Contact Information")
    position = fields.Char(string="Position")
    qualification = fields.Binary(string="Qualification Document")
    is_employee=fields.Boolean(string='Is Employee')
