
from odoo import fields, models , api,_

class Pharmacy(models.Model):
    _name = "pharma.pharmacy"
    _rec_name = 'fname'

    pharmacy_id = fields.Integer(string=_('Pharmacy ID'))
    fname = fields.Char(string=_("First Name"))
    lname = fields.Char(string=_("Last Name"))
    fullname = fields.Char(string=_("Full Name"), compute='_compute_fullname')
    address = fields.Char(string=_("Address"))
    contact_info = fields.Text(string=_("Contact Information"))
    opening_hours = fields.Float(string=_("Opening Hours"))
    employees = fields.One2many('pharma.employee', 'pharmacy_id', string=_("Employees"))


    def unlink(self):
        for rec in self : 
            for employee_id in self.employees:
                if employee_id.is_employee == False:
                    rec.employees= [(3,rec.employee_id.id)]




    @api.depends('fname', 'lname')
    def _compute_fullname(self):
        for rec in self:
            rec.fullname = f"{rec.fname} {rec.lname}"

    @api.onchange('address')
    def address_update(self):
        for rec in self:
            if not rec.address:
                pass
            else:
                return {
                    'warning': {
                        'title': ('Address change Warning'),
                        'message': 'Address is changed to %s' % (rec.address)
                    }
                }

    # @api.constrains('pharmacy_id')
    # def _check_crud_op(self):
    #     for rec in self:
    #         rec.employees = [(0, 0, {

    #         })]
    #         self.env['pharma.employee'].create({
    #             'name': 'New Employee',
    #             'position': 'Manager',
    #             'pharmacy_id': self.id
    #         })

    #     reads = self.env['pharma.employee'].search([('name', '=', 'New Employee')])
    #     for read in reads:
    #         print("hello")
    #         print(read.name, read.position)




            # update = self.env['pharma.employee'].search([('name', '=', 'New Employee')])

            # if update:
            #     update.write({
            #         'name': 'New Employee',
            #         'position': 'Manager'
            #     })
