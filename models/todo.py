from odoo import models, fields


class ToDo(models.Model):
    _name = "todo"
    _description = "todo"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Task Name", required=True, tracking=True)
    partner_id = fields.Many2one("res.partner", string="Assign To", tracking=True)
    description = fields.Text(string="Description", required=True, tracking=True)
    date = fields.Date(string="Date", required=True, tracking=True)
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'IN Progress'),
        ('completed', 'Completed')

    ], string='Status', default='new', tracking=True)
