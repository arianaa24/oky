# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import base64
import io
import zipfile

class WizardDownloadInvoices(models.TransientModel):
    _name = 'oky.download_invoices'
    
    account_move_ids = fields.Many2many("account.move", string="Facturas", required=True)
    
    name = fields.Char('Nombre archivo')
    archivo = fields.Binary('Archivo')
    
    def print_zip_file(self):
        for w in self:
            dic = {}
            dic['account_move_ids'] = w['account_move_ids']
            
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w') as zip_archive:
                for invoice in dic['account_move_ids']:
                    file_name = str(invoice.partner_id.state_id.name) + ', ' + str(invoice.partner_id.name) + ', ' + str(invoice.name).replace("/", "-") + '.pdf'
                    report = self.env['ir.actions.report']._render_qweb_pdf("oky.oky_account_invoice1", invoice.id)
                    zip_archive.writestr(file_name, report[0])
            
            datos = base64.b64encode(zip_buffer.getvalue())
            self.write({'archivo':datos, 'name':'facturas_individuales'})
        return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'oky.download_invoices',
            'res_id': self.id,
            'view_id': False,
            'type': 'ir.actions.act_window',
            'target': 'new',
        }