from odoo import api, fields, models, _


class ScrumSprint (models.Model):
    _name = 'scrum.sprint'

    name = fields.Char(string='Sprint name')
    date_init = fields.Date(string='Sprint Start')
    date_end = fields.Date(string='Sprint End')
    team_id = fields.Many2one('scrum.team', string='Scrum team')
    active = fields.Boolean(string='Active',default=True)

    @api.multi
    def toggle_active(self):
        """ Inverse the value of the field ``active`` on the records in ``self``. """
        for record in self:
            record.active = not record.active