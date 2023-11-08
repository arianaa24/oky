# -*- coding: utf-8 -*-

from odoo import api, models
from odoo.addons.l10n_gt_extra import a_letras
import logging

class ReportAbstractInvoice(models.AbstractModel):
    _name = 'oky.abstract.reporte_account_invoice'

    def a_letras(self, monto):
        return a_letras.num_a_letras(monto)

    def tipo_cambio(self, factura):
        total = 0
        tipo_cambio = 1
        for line in factura.line_ids:
            if line.account_id.reconcile:
                total += line.debit - line.credit
        if factura.amount_total != 0:
            tipo_cambio = abs(total / factura.amount_total)
        return tipo_cambio

    def impuestos(self, factura):
        isv_por_pagar = 0
        isv_por_cobrar = 0
        iva_retenido = 0
        sujeto_no_excluido = 0
        isr_10 = 0
        for tax in factura.line_ids.tax_line_id:
            if tax.name == 'ISV por Cobrar' or tax.name == 'IVA por Cobrar':
                isv_por_cobrar += tax.amount
            elif tax.name == 'ISV por Pagar' or tax.name == 'IVA por Pagar':
                isv_por_pagar += tax.amount
            elif tax.name == '(-) IVA Retenido':
                iva_retenido += tax.amount
            elif tax.name == 'Sujeto No Excluido':
                sujeto_no_excluido += tax.amount
            elif tax.name == 'ISR 10%':
                isr_10 += tax.amount

        dict = {
            'isv_por_pagar': isv_por_pagar,
            'isv_por_cobrar': isv_por_cobrar,
            'iva_retenido': iva_retenido,
            'sujeto_no_excluido': sujeto_no_excluido,
            'isr_10': isr_10,
        }
        return dict

    @api.model
    def _get_report_values(self, docids, data=None):
        model = 'account.move'
        docs = self.env[model].browse(docids)

        return {
            'doc_ids': docids,
            'doc_model': model,
            'docs': docs,
            'impuestos': self.impuestos,
            'tipo_cambio': self.tipo_cambio,
            'a_letras': self.a_letras,
        }

class ReportInvoice1(models.AbstractModel):
    _name = 'report.oky.reporte_account_invoice1'
    _inherit = 'oky.abstract.reporte_account_invoice'

class ReportInvoice2(models.AbstractModel):
    _name = 'report.oky.reporte_account_invoice2'
    _inherit = 'oky.abstract.reporte_account_invoice'

class ReportInvoice3(models.AbstractModel):
    _name = 'report.oky.reporte_account_invoice3'
    _inherit = 'oky.abstract.reporte_account_invoice'

class ReportInvoice4(models.AbstractModel):
    _name = 'report.oky.reporte_account_invoice4'
    _inherit = 'oky.abstract.reporte_account_invoice'

class ReportInvoice5(models.AbstractModel):
    _name = 'report.oky.reporte_account_invoice5'
    _inherit = 'oky.abstract.reporte_account_invoice'

class ReportInvoice6(models.AbstractModel):
    _name = 'report.oky.reporte_account_invoice6'
    _inherit = 'oky.abstract.reporte_account_invoice'