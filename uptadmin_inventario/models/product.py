from odoo import api, fields, models
from datetime import datetime, timedelta

class ProductProduct(models.Model):
    _inherit = 'product.product'
    

class ProductTemplate(models.Model):
    _inherit = 'product.template'
