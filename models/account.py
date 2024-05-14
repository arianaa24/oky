# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class AccountJournal(models.Model):
    _inherit = "account.journal"

    cai = fields.Char('C.A.I.')
    numero_desde = fields.Char('Número desde')
    numero_hasta = fields.Char('Número hasta')
    fecha_limite = fields.Date('Fecha límite de emisión')
