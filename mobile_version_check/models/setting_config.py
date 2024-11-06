from odoo import fields, models, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    _description = 'Res Config Settings'

    ios_package_name = fields.Char(config_parameter='ios_package_name')
    android_package_name = fields.Char(config_parameter='android_package_name')
    force_update = fields.Boolean(default=False, config_parameter='force_update')