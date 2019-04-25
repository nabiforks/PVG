import calendar
from odoo import models, fields, api, _


class accrStudentNutritionDetails(models.Model):
    _name = "accr.student.nutrition.details"
    _description = "Student Nutrition Details"

    student = fields.Many2one('x_student', string=u'Student', required=True, ondelete='set null', )
    name = fields.Char(compute='_compute_name', string=u'Name', readonly=True, store=True, )
    age = fields.Char(related='student.x_studio_age', string=u"Age", readonly=True, store=False, )
    diagnosis = fields.Text(related='student.x_studio_diagnosis', string=u'Diagnosis', readonly=True, store=False, )
    residential_section = fields.Many2one(related='student.x_studio_residential_sections', string=u'Residential Section', readonly=True, store=False, )
    medications = fields.One2many(related='student.x_studio_field_jm5yW', string=u'Medications', readonly=True, store=False, )
    food_preferences = fields.One2many('accr.student.food.preferences', 'nutrition_details', string=u'Food Preferences', )
    food_intolerance = fields.One2many('accr.student.food.intolerance', 'nutrition_details', string=u'Food Intolerance', )

    height = fields.Integer(string=u'Height', required=True, )
    weight = fields.Integer(string=u'Weight', required=True, )
    diet = fields.Many2one('accr.diet', string=u'Diet', )
    requirements = fields.Many2one('accr.nutrition.requirements', string=u'Requirements', )
    physical_activity = fields.Many2one('accr.physical.activity', string=u'Physical Activity', )
    water_intake = fields.Many2one('accr.water.intake', string=u'Water Intake', )
    nutritional_needs = fields.Many2one('accr.nutritional.needs', string=u'Nutritional Needs', )

    @api.multi
    @api.depends('student', 'create_date')
    def _compute_name(self):
        for record in self:
            record.name = record.student.display_name + ' - '+ record.create_date.strftime("%Y-%m-%d")