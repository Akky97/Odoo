# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PosOrder(models.Model):
    _name = "pos.order"
    _inherit = ['pos.order', 'mail.thread', 'mail.activity.mixin']

    def get_lot_available(self, msg, product):
        rec = self.env['stock.production.lot'].sudo().search([('name', '=', msg), ('product_id', '=', product)])
        if rec:
            return True
        else:
            return False

    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, **kwargs):
        return super(PosOrder, self.with_context(mail_post_autofollow=True)).message_post(**kwargs)

    def create(self, values):
        rec = super().create(values)
        for line in rec.lines:
            message = ""
            for lot in line.pack_lot_ids:
                if lot.lot_name:
                    vv = self.env['stock.production.lot'].sudo().search(
                        [('name', '=', lot.lot_name), ('product_id', '=', line.product_id.id)])
                    if not vv:
                        message += f"{line.product_id.name} Lot No. {lot.lot_name} is unavailable in stock,"
            if message:
                rec.message_post(body=message)
        return rec
