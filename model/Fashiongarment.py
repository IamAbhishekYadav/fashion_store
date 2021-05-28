from odoo import models, fields, api

class FashionGarment(models.Model):
    _name = 'fashion.fashiongarment'
    name=fields.Char(string='Name')
    garment_type=fields.Selection([('tshirt','Tshirt'),
                                   ('shirt','Shirt'),
                                   ('jeans','Jeans'),
                                   ('short','Shirt'),
                                   ('shoe','Shoe')],string='Garment Type')
    brand=fields.Selection([('nike','nike'),
                            ('levis','Levis'),
                            ('adidas','Adidas'),
                            ('wrogn','Wrogn'),
                            ('pepe','Pepe')],string='Brand')
    quantity=fields.Integer(string='Quantity')
    price=fields.Integer(string='Price')
