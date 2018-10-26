# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)
import werkzeug
import json

from openerp import api, fields, models

class SaveMailMassMailing(models.Model):

    _inherit = "mail.mass_mailing"
    
    m_campaign_id = fields.Many2one('marketing.campaign', string="Marketing Campaign")
    
    @api.multi
    def save_to_campaign(self):
        partner_model = self.env['ir.model'].search([('model','=','mail.mass_mailing.contact')])[0]
        new_mail_template = self.env['mail.template'].create({'name': self.name + " Mail Template", 'model_id': partner_model.id, 'body_html': self.body_html, 'subject': self.name, 'email_from': self.email_from})
        return {
	    'view_type': 'form',
	    'view_mode': 'form',
	    'res_model': 'mail.template',
	    'target': 'current',
	    'res_id': new_mail_template.id,
	    'type': 'ir.actions.act_window'
	}
