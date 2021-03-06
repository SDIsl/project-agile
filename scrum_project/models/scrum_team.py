from odoo import api, fields, models, _
from odoo import tools, _
from odoo.modules.module import get_module_resource
import base64


class ScrumTeam (models.Model):
    _name = 'scrum.team'

    @api.model
    def _default_image(self):
        image_path = get_module_resource('scrum_project', 'static/src/img', 'default_image.png')
        return tools.image_resize_image_big(base64.b64encode(open(image_path, 'rb').read()))

    name = fields.Char(string='Name SCRUM team', required='True')
    user_ids = fields.Many2many(comodel_name='res.users', string='Team components')

    # image: all image fields are base64 encoded and PIL-supported
    image = fields.Binary(
        "Photo", default=_default_image, attachment=True,
        help="This field holds the image used as photo for the team, limited to 1024x1024px.")
    image_medium = fields.Binary(
        "Medium-sized photo", attachment=True,
        help="Medium-sized photo of the team. It is automatically "
             "resized as a 128x128px image, with aspect ratio preserved. "
             "Use this field in form views or some kanban views.")
    image_small = fields.Binary(
        "Small-sized photo", attachment=True,
        help="Small-sized photo of the team. It is automatically "
             "resized as a 64x64px image, with aspect ratio preserved. "
             "Use this field anywhere a small image is required.")

    stage_ids = fields.Many2many('project.task.type', string='Stage')
    current_sprint = fields.Many2one(comodel_name='scrum.sprint',
                                     string='Current Sprint',
                                     compute="_compute_current_sprint")
    sprints_count = fields.Integer(string='Total Sprints',
                                   compute="_compute_count")

    @api.multi
    def _compute_current_sprint(self):
        for team in self:
            sprint_obj = self.env['scrum.sprint'].search(
                [('team_id', '=', team.id), ("active", "=", True)],
                order="date_init desc", limit=1)
            team.current_sprint = sprint_obj or False

    @api.multi
    def _compute_count(self):
        for team in self:
            total = self.env['scrum.sprint'].search_count(
                [('team_id', '=', team.id)])
            team.sprints_count = total

    @api.model
    def create(self, vals):
        tools.image_resize_images(vals)
        return super(ScrumTeam, self).create(vals)

    @api.multi
    def write(self, vals):
        tools.image_resize_images(vals)
        return super(ScrumTeam, self).write(vals)

    def scrum_team_kanban_act(self):
        # ODOO ME VACILA CON EL CONTEXTO --- NOTAS, BORRAR ---
        context = {
                'default_group_by': 'scrum_stage_id',
                'search_default_scrum_team_id': [self.id],
                'default_scrum_team_id': self.id,
                'search_default_scrum_sprint_id': [self.current_sprint.id],
                'default_scrum_sprint_id': self.current_sprint.id,
        }
        domain = [('scrum_sprint_id', '=', self.current_sprint.id)]
        scrum_task_kanban_ref = self.env.ref('scrum_project.project_task_scrum_view_kanban').id
        return {
            "name": _("Sprint Dashboard")+"/"+self.current_sprint.name,
            "type": "ir.actions.act_window",
            "res_model": "project.task",
            "view_mode": "form",
            "view_type": "form",
            "views": [[scrum_task_kanban_ref, "kanban"], [False, "form"], [False, "tree"],
                      [False, "search"]],
            "domain": domain,
            "context": context,
            "target": "current"
        }
