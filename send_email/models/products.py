from odoo import models


class ResPartner(models.Model):
    _inherit = "product.product"

    def action_product_send(self):
        print("\n\n\nhello")
        ''' Opens a wizard to compose an email, with relevant mail template loaded by default '''
        self.ensure_one()
        template_id = self.env.ref('send_email.product_mail_template').id
        print("\n\n\nid ", template_id)
        lang = self.env.context.get('lang')
        template = self.env['mail.template'].browse(template_id)
        if template.lang:
            lang = template._render_lang(self.ids)[self.id]
        print("\n\n\nid ", template)

        ctx = {
            'default_model': 'product.product',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'custom_layout': "mail.mail_notification_paynow",
            'proforma': self.env.context.get('proforma', False),
            'force_email': True,
            'model_description': self.with_context(lang=lang),
        }
        print("\n\n\nlast", ctx)
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(False, 'form')],
            'view_id': False,
            'target': 'new',
            'context': ctx,
        }

    # } def action_product_send(self):
    # print("\n\n\nhello")
    # self.ensure_one()
    # template_id = self.env.ref('send_email.product_mail_template')
    # # template = self.env['mail.template'].browse(template_id)
    # # if template.lang:
    # #     lang = template._render_lang(self.ids)[self.id]
    # ctx = {
    #     'default_model': 'product.product',
    #     'default_res_id': self.ids[0],
    #     'default_use_template': bool(template_id),
    #     'default_template_id': template_id,
    #     'default_composition_mode': 'comment',
    #     'mark_so_as_sent': True,
    #     'custom_layout': "mail.mail_notification_paynow",
    #     'proforma': self.env.context.get('proforma', False),
    #     'force_email': True,
    #     # 'model_description': self.with_context(lang=lang).type_name,
    # }
    #
    # return {
    #     'type': 'ir.actions.act_window',
    #     'view_mode': 'form',
    #     'res_model': 'mail.compose.message',
    #     'views': [(False, 'form')],
    #     'view_id': False,
    #     'target': 'new',
    #     'context': ctx,
    # }
    #
    # def action_quotation_send(self):
    #     ''' Opens a wizard to compose an email, with relevant mail template loaded by default '''
    #     self.ensure_one()
    #     template_id = self._find_mail_template()
    #     lang = self.env.context.get('lang')
    #     template = self.env['mail.template'].browse(template_id)
    #     if template.lang:
    #         lang = template._render_lang(self.ids)[self.id]
    #     ctx = {
    #         'default_model': 'sale.order',
    #         'default_res_id': self.ids[0],
    #         'default_use_template': bool(template_id),
    #         'default_template_id': template_id,
    #         'default_composition_mode': 'comment',
    #         'mark_so_as_sent': True,
    #         'custom_layout': "mail.mail_notification_paynow",
    #         'proforma': self.env.context.get('proforma', False),
    #         'force_email': True,
    #         'model_description': self.with_context(lang=lang).type_name,
    #     }
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'view_mode': 'form',
    #         'res_model': 'mail.compose.message',
    #         'views': [(False, 'form')],
    #         'view_id': False,
    #         'target': 'new',
    #         'context': ctx,
    #     }
