from odoo import http
from odoo.http import request

class CoursesController(http.Controller):
    @http.route('/courses', auth='public', website=True)
    def display_courses(self, **kw):
        courses = request.env['courses.course'].search([])
        return request.render('Courses.template_courses', {'courses': courses})


class CoursesController(http.Controller):
    @http.route('/courses/<int:course>', auth='public', website=True)
    def display_courses(self, course):
        courses = request.env['courses.course'].browse(course)
        return request.render('Courses.template_courses_a', {'courses': courses})
