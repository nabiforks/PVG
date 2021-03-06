from odoo import models, fields, api, _


class accrStudentFoodPreferences(models.Model):
    _name = "accr.student.food.preferences"
    _description = "Food prefernces menu for student"

    # student = fields.Many2one('x_student', string=u'Student', required=True, )
    # nutrition_details = fields.Many2one('accr.student.nutrition.details', string=u'Nutrition Details',)
    nutrition_student = fields.Many2one('accr.nutrition.student', string=u'Nutrition Student',)
    student = fields.Many2one(related='nutrition_student.student', string=u'Student', required=True, )
    food = fields.Many2many('accr.food','accr_food_food_preferences_rel', 'food_preferences_id', 'accr_food_id', string="Food", required=True, )
    food_group = fields.Many2one('accr.food.group', string=u'Food Group', required=True, )
    # name = fields.Char('Name', compute='_compute_name', )
    preference = fields.Selection(
        [('Like', 'Like'), ('Dislike', 'Dislike')], string=u'Preference', required=True,)

    @api.multi
    @api.depends('student', 'food_group')
    def _compute_name(self):
        for record in self:
            record.name = record.student.display_name + ' - ' + record.food_group.display_name + ' - ' + record.preference.Selection
