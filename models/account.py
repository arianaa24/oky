# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from base64 import b64encode
import urllib

class AccountJournal(models.Model):
    _inherit = "account.journal"

    cai = fields.Char('C.A.I.')
    numero_desde = fields.Char('Número desde')
    numero_hasta = fields.Char('Número hasta')
    fecha_limite = fields.Date('Fecha límite de emisión')

class AccountMove(models.Model):
    _inherit = "account.move"
    
    pdf_fel_file = fields.Binary('PDF FEL', copy=False)
    pdf_fel_name = fields.Char('Nombre PDF FEL', default='pdf_fel.pdf')
    
    def _post(self, soft=True):
        res = super(AccountMove, self)._post(soft)
        for rec in res:
            if rec.pdf_fel:
                file_name = str(rec.partner_id.state_id.name) + ', ' + str(rec.partner_id.name) + ' - ' + str(rec.name) + '.pdf'
                response = urllib.request.urlopen(rec.pdf_fel)
                data = response.read()
                rec.write({'pdf_fel_file':b64encode(data), 'pdf_fel_name':file_name})
        return res

    def post(self):
        res = super(AccountMove, self).post()
        for rec in res:
            if rec.pdf_fel:
                file_name = str(rec.partner_id.state_id.name) + ', ' + str(rec.partner_id.name) + ' - ' + str(rec.name) + '.pdf'
                response = urllib.request.urlopen(rec.pdf_fel)
                data = response.read()
                rec.write({'pdf_fel_file':b64encode(data), 'pdf_fel_name':file_name})
        return res