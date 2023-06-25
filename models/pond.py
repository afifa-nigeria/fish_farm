from odoo import models, fields


class Pond(models.Model):
    _name = 'pond'
    _description = 'Pond'

    name = fields.Char(string='Pond Name', required=True)
    capacity = fields.Float(string='Capacity', required=True)
    location = fields.Char(string='Location')
    water_source = fields.Char(string='Water Source')
    temperature = fields.Float(string='Temperature')
    pH = fields.Float(string='pH')

    # Optional relationships
    #fish_stock_ids = fields.One2many('fish_stock_intake', 'pond_ids', string='Fish Stocks')

