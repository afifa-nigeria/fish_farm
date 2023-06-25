from odoo import models, fields


class FishStockIntake(models.Model):
    _name = 'fish_farm.fish_stock.intake'
    _description = 'Fish Stock Intake'

    species = fields.Char(string='Species', required=True)
    quantity = fields.Float(string='Quantity', required=True)
    size = fields.Char(string='Size')
    source = fields.Char(string='Source')
    intake_date = fields.Date(string='Intake Date', default=fields.Date.today())

    # Add any other fields as per your requirements

    # Optional relationships
    #pond_ids = fields.Many2many('pond', string='Ponds')

