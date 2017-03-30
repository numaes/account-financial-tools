# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __odoo__.py file in module root
# directory
##############################################################################
from odoo import fields, models, api


class ResCompany(models.Model):
    _inherit = "res.company"

    @api.model
    def _get_localizations(self):
        return [('generic', 'Generic')]

    _localization_selection = (
        lambda self, *args, **kwargs: self._get_localizations(
            *args, **kwargs))

    localization = fields.Selection(
        _localization_selection,
        'Localization',
    )
