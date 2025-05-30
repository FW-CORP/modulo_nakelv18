from odoo import models, api

class ProductTemplate(models.Model):
    _inherit = "product.template"

    # Hereda la alícuota cuando se selecciona una categoría
    @api.onchange("categ_id")
    def _onchange_categ_id_set_internal_tax(self):
        for product in self:
            if (
                product.categ_id
                and product.categ_id.internal_tax_id
                and not product.taxes_id
            ):
                product.taxes_id = [(6, 0, [product.categ_id.internal_tax_id.id])]

    # Hereda la alícuota en la creación masiva
    @api.model_create_multi
    def create(self, vals_list):
        products = super().create(vals_list)
        for product in products:
            if (
                product.categ_id
                and product.categ_id.internal_tax_id
                and not product.taxes_id
            ):
                product.taxes_id = [(6, 0, [product.categ_id.internal_tax_id.id])]
        return products
