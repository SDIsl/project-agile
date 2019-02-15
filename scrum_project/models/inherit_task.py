
from odoo import api, fields, models, _


class ProjectTask (models.Model):

    _inherit = 'project.task'

    is_user_story = fields.Boolean(string='Is user story', help=_(
        'Mark if this taks is a user history'))
    scrum_what = fields.Text(string='What to do?')
    scrum_who = fields.Text(string='For whom?')
    scrum_for_what = fields.Text(string='For What?')
    scrum_complexity = fields.Integer(
        string='Complexity', help=_('Score the complexity of the task'))
    scrum_priority = fields.Selection(string='Task priority', selection=[(
        '0', 'Normal'), ('1', 'Baja'), ('2', 'Alta'), ('3', 'Muy Alta')])
    scrum_value = fields.Integer(string='Value')
    scrum_sprint_id = fields.Many2one('scrum.sprint', string='Sprint')
    scrum_team_id = fields.Many2one(related='scrum_sprint_id.team_id', readonly='True')
    scrum_stage_id = fields.Many2one('project.task.type', string='Stage')
    