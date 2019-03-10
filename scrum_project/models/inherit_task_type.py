from odoo import api, fields, models, _


class TaskType (models.Model):
    _inherit = 'project.task.type'

    scrum_team_ids = fields.Many2many('scrum.team', string='Scrum teams')