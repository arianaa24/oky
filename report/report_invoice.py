# -*- coding: utf-8 -*-

from odoo import api, models
import odoo.addons.l10n_gt_extra.a_letras
import logging

class ReportAbstractInvoice(models.AbstractModel):
    _name = 'oky.abstract.reporte_account_invoice'

    nombre_reporte = ''

    def tipo_cambio(self, factura):
        total = 0
        tipo_cambio = 1
        for line in factura.move_id.line_ids:
            if line.account_id.reconcile:
                total += line.debit - line.credit
        if factura.amount_total != 0:
            tipo_cambio = abs(total / factura.amount_total)
        return tipo_cambio

    def impuestos(self, factura):
        isv_por_pagar = 0
        isv_por_cobrar = 0
        isv_18 = 0
        for tax in factura.tax_line_ids:
            if tax.name == 'ISV por Cobrar':
                isv_por_pagar += tax.amount
            elif tax.name == 'ISV por Pagar':
                isv_por_cobrar += tax.amount
            elif tax.name == 'ISR 10%':
                isv_18 += tax.amount

        dict = {
            'isv_por_pagar': isv_por_pagar,
            'isv_por_cobrar': isv_por_cobrar,
            'isv_18': isv_18,
        }
        return dict

    @api.model
    def _get_report_values(self, docids, data=None):
        self.model = 'account.invoice'
        docs = self.env[self.model].browse(docids)

        return {
            'doc_ids': docids,
            'doc_model': self.model,
            'docs': docs,
            'impuestos': self.impuestos,
            'tipo_cambio': self.tipo_cambio,
            'a_letras': odoo.addons.l10n_gt_extra.a_letras,
        }

class ReportInvoice1(models.AbstractModel):
    _name = 'report.oky.reporte_account_invoice1'
    _inherit = 'oky.abstract.reporte_account_invoice'

    nombre_reporte = 'oky.reporte_account_invoice1'

class ReportInvoice2(models.AbstractModel):
    _name = 'report.oky.reporte_account_invoice2'
    _inherit = 'oky.abstract.reporte_account_invoice'

    nombre_reporte = 'oky.reporte_account_invoice2'
