from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class UpdateLooker(models.Model):
    _name = 'update.looker'
    _description = 'Update Looker'

    name = fields.Char(string="Name")
    input_url = fields.Char(string="Input URL Embed")
    aktif = fields.Boolean(string="Active", default= False)
 
    
    def get_URL(self):
        record = self.search([('aktif', '=', True)], limit=1)
        if record:
            return record.input_url

    @api.constrains('aktif')
    def _check_only_one_active(self):
        if self.aktif:
            active_records = self.search([('aktif', '=', True), ('id', '!=', self.id)])
            if active_records:
                raise ValidationError("Hanya satu looker yang bisa aktif.")