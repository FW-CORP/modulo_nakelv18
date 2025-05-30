from odoo import models, fields

class ProductCategory(models.Model):
    _inherit = "product.category"

    internal_tax_id = fields.Many2one(
        "account.tax",
        string="Impuesto interno por defecto",
        domain=[("tax_group_id.name", "=", "Impuestos Internos")],
        help="Alicuota interna que se aplicará a los productos de esta categoría si no tienen impuestos definidos."
    )
