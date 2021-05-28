from odoo import models, fields, api

class OrderLine(models.Model):
    _name = 'fashion.orderline'
    order_date=fields.Datetime(string='Order Date')
    quantity=fields.Integer(string='Quantity')
    price=fields.Integer(string='Price')
    total=fields.Integer(string='Total Price')
    garment = fields.Many2one('fashion.fashiongarment',string='Garment')