from odoo import api, fields, models, exceptions, _
from odoo.exceptions import UserError, ValidationError
import gspread
# from google.oauth2.service_account import Credentials
from datetime import datetime, date
import json
import time
import logging
_logger = logging.getLogger(__name__)

class QueryDeluxeGooglesheet(models.Model):
    _inherit = 'querydeluxe'

    sheets_name = fields.Char(string='Sheets Name')
    schedule_update_spreadsheet = fields.Boolean(string='Update Otomatis', default = False)
    spreadsheets_code = fields.Char(string='Spreadsheets ID')
    # sheets_name = fields.Selection([
    #     ('Data Postgres 1', 'Data Postgres 1'), 
    #     ('Data Postgres 2', 'Data Postgres 2'), 
    #     ('Equipment', 'Equipment'), 
    #     ('Equipment Produksi', 'Equipment Produksi'),
    #     ('MTBF & MTTR', 'MTBF & MTTR'),
    #     ], string='Sheets Name' )
    # spreadsheets_name = fields.Selection([
    #     ('Python_Script', 'Python_Script'),
    #     ], string='Spreadsheets Name' )
    # gsheets = fields.Text(string='Type a query to Googlesheets')


    def get_data_and_update_sheet(self):
        # Mengambil data dari Query
        records = self.get_data()

        # Mengupdate Google Sheet dengan data yang diambil
        self.update_google_sheet(records)


    def get_credentials_code(self):
        # Mendapatkan record dari model credentialsgooglesheets
        credentials = self.env['credentialsgooglesheets'].search([('aktif', '=', True)], limit=1)
        
        # Memeriksa apakah record ada
        if credentials:
            code = json.loads(credentials.credentials_code)
            return code

    def get_data(self):
        if self.name:
            self.tips = False
            self.message_post(body=str(self.name))

            headers = []
            datas = []

            self.env.cr.execute(self.name)

            if self.env.cr.description:
                headers = [d[0] for d in self.env.cr.description]
                datas = self.env.cr.fetchall()

                # Mengonversi nilai datetime ke string format yang sesuai
                formatted_datas = []
                for row in datas:
                    formatted_row = []
                    for value in row:
                        if isinstance(value, datetime):
                            formatted_row.append(value.strftime('%Y-%m-%d %H:%M:%S'))  # Ubah sesuai format yang Anda inginkan
                        elif isinstance(value, date):
                            formatted_row.append(value.strftime('%Y-%m-%d'))
                        else:
                            formatted_row.append(value)
                    formatted_datas.append(formatted_row)

                # Siapkan values untuk dimasukkan ke Google Sheets
                values = [headers] + formatted_datas
                return values
    
    def update_google_sheet(self, values):
        starttime = time.time()
        try:
            # Menghubungkan ke Google Sheets API menggunakan kredensial service account
            credentials = self.get_credentials_code()  # mengambil kredensial service account.
            client = gspread.service_account_from_dict(credentials)
            workbook = client.open_by_key(self.spreadsheets_code)
            
            # Nama worksheet yang akan diperiksa atau dibuat
            new_worksheet_name = self.sheets_name

            if new_worksheet_name in [ws.title for ws in workbook.worksheets()]:
                sheet = workbook.worksheet(new_worksheet_name)
            else:
                sheet = workbook.add_worksheet(new_worksheet_name, rows=len(values), cols=len(values[0]))

            # Hapus isi sheet kemudian update dengan data terbaru
            sheet.clear()

            # gspread==3.x.x
            sheet.update('A1', values)

            # gspread==x.x.x
            # sheet.update(range_name='A1', values=values)

            sheet.format('1', {'textFormat': {'bold': True}})
            endtime = time.time()
            duration = endtime - starttime
            _logger.info("Durasi update Google Sheet = %.2f detik", duration)
        except:
            raise ValidationError("Cek Credentials dan Spreadsheets ID!")

    def cron_scheduled_update_googlesheets(self):
        records = self.search([('schedule_update_spreadsheet', '=', True)])
        for record in records:
            record.get_data_and_update_sheet()

    def toggle_cron(self, active):
        cron = self.env.ref('query_deluxe_inherit.ir_cron_update_sheet')
        if cron:
            cron.write({'active': active})

    @api.constrains('schedule_update_spreadsheet')
    def _check_schedule_update_spreadsheet(self):
        records = self.search([('schedule_update_spreadsheet', '=' , True)])
        if records:
            self.toggle_cron(True)
        else:
            self.toggle_cron(False)