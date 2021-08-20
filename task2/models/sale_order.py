
from odoo import fields, models
from odoo.tools.translate import _


class TotalSaleOrder(models.Model):
	_inherit = "sale.order"

	total_capacity = fields.Float(string=_("Total Capacity"), readonly=True)

	def calculate_total_capacity(self):
		# for order in self:
		total_capacity = 0
		for line in self.order_line:
			total_capacity += line.max_qty_allowed

		self.update({"total_capacity": total_capacity})


class SaleOrder(models.Model):
	_inherit = "sale.order.line"

	# product_id = fields.Many2one("product.product", string="id")
	max_qty_allowed = fields.Float(
		related="product_id.qty_on_order", string=_("Max Qty Allowed"), store=True
	)
