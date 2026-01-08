from odoo import models, fields
from odoo.exceptions import UserError

class GiftCardCancel(models.TransientModel):
    _name = 'gift.card.cancel'
    _description = 'Gift Card Cancellation Wizard'

    gift_card_code = fields.Char(
        string='Gift Card Code',
        required=True,
        help='Enter the gift card code to cancel'
    )

    def action_cancel_gift_card(self):
        """Cancel the gift card by setting points to 0"""
        self.ensure_one()
        
        if not self.gift_card_code:
            raise UserError('Please enter a gift card code.')
        
        # Search for the gift card
        gift_card = self.env['loyalty.card'].search([
            ('code', '=', self.gift_card_code)
        ], limit=1)
        
        if not gift_card:
            raise UserError(f'Gift card with code "{self.gift_card_code}" not found.')
        
        # Store old balance for message
        old_balance = gift_card.points
        
        # Set points to 0
        gift_card.write({'points': 0.0})
        
        # Return success message
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Gift Card Cancelled',
                'message': f'Gift card "{self.gift_card_code}" has been cancelled. Balance changed from {old_balance} to 0.',
                'type': 'success',
                'sticky': False,
            }
        }