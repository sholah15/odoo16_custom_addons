from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

class CredentialsGooglesheets(models.Model):
    _name = "credentialsgooglesheets"
    _description = "upload credentials"

    name = fields.Char(string='Name')
    credentials_type = fields.Selection([
        ('service_account', 'Service Account'), 
        ], string='Tipe' )
    credentials_code = fields.Json(string='Code')
    aktif = fields.Boolean('Active', default= False)

    @api.constrains('aktif')
    def _check_only_one_active(self):
        if self.aktif:
            active_records = self.search([('aktif', '=', True), ('id', '!=', self.id)])
            if active_records:
                raise ValidationError("Hanya satu credentials yang boleh aktif.")
