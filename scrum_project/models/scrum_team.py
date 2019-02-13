from odoo import api, fields, models, _


class ScrumTeam (models.Model):
    _name = 'scrum.team'

    name = fields.Char(string='Name SCRUM team', required='True')
    user_ids = fields.Many2many(comodel_name='res.users', string='Team components')
    image = fields.Binary(string='Image')
    stage_ids = fields.Many2many('project.task.type', string='Stage')


