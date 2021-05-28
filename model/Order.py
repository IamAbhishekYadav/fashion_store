from odoo import models, fields, api

class Order(models.Model):
    _name = 'fashion.order'
    date=fields.Date(string='Date')
    order total=fields.Float(string='Total')


    def calculate_total_order(self):
        total=0
        print(self.orderline)
        for line in self.orderline:
            total+=line.total
        self.write({'order total':total})
        return True