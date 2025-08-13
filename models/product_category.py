from odoo import models, fields

class ProductCategory(models.Model):
	_inherit = "product.category"
	internal_tax_id = fields.Many2one(
    	"account.tax",
    	domain=[("tax_group_id.name", "=", "Impuestos Internos")],
)
