from odoo import models, fields, api
from odoo.tools import format_amount
from odoo.tools.translate import _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    cost_tax_string = fields.Char(compute="_compute_cost_tax_string")

    @api.depends("supplier_taxes_id", "standard_price")
    @api.depends_context("company")
    def _compute_cost_tax_string(self):
        for record in self:
            record.cost_tax_string = record._construct_cost_tax_string(
                record.standard_price
            )

    def _construct_cost_tax_string(self, price):
        currency = self.cost_currency_id
        taxes = self.supplier_taxes_id._filter_taxes_by_company(self.env.company)
        if not taxes:
            return " "
        res = taxes.compute_all(price, currency=currency, product=self)
        joined = []
        included = res["total_included"]
        if currency.compare_amounts(included, price):
            joined.append(
                _(
                    "%(amount)s Impuestos Incluidos",
                    amount=format_amount(self.env, included, currency),
                )
            )
        excluded = res["total_excluded"]
        if currency.compare_amounts(excluded, price):
            joined.append(
                _(
                    "%(amount)s Impuestos Excluidos",
                    amount=format_amount(self.env, excluded, currency),
                )
            )
        return f"(= {', '.join(joined)})" if joined else " "


class ProductProduct(models.Model):
    _inherit = "product.product"

    cost_tax_string = fields.Char(compute="_compute_cost_tax_string")

    @api.depends(
        "product_tmpl_id", "product_tmpl_id.supplier_taxes_id", "standard_price"
    )
    @api.depends_context("company")
    def _compute_cost_tax_string(self):
        for record in self:
            record.cost_tax_string = record.product_tmpl_id._construct_cost_tax_string(
                record.standard_price
            )
