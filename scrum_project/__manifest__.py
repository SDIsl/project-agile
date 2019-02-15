# SDI
# © 2019 Jorge Luis Quinteros <jquinteros@sdi.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'SCRUM Project',
    'version': '11.0.1.0.0',
    'category': 'Project Agile',
    'author': 'SDi Soluciones Informáticas',
    'summary': """ Create SCRUM environment""",
    'license': 'AGPL-3',
    'depends': [
        'project',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/inherit_task.xml',
        'views/scrum_sprint.xml',
        'views/scrum_project.xml',
        'views/scrum_team.xml',
        'views/inherit_task_type.xml',
    ],
    'installable': True,
    'application': False,
}
