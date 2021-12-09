# -*- coding: utf-8 -*-

from odoo import api, models

class ReportAbstractInvoice(models.AbstractModel):
    _name = 'oky.abstract.reporte_account_invoice'

    nombre_reporte = ''

    @api.model
    def _get_report_values(self, docids, data=None):
        self.model = 'account.invoice'
        docs = self.env[self.model].browse(docids)

        return {
            'doc_ids': docids,
            'doc_model': self.model,
            'docs': docs,
        }

class ReportInvoice1(models.AbstractModel):
    _name = 'report.oky.reporte_account_invoice1'
    _inherit = 'oky.abstract.reporte_account_invoice'

    nombre_reporte = 'oky.reporte_account_invoice1'
