import random
import string

from odoo import api, fields, models
from odoo.tools.translate import _


class Product(models.Model):
	_inherit = "product.template"

	# attrs = "{'invisible': [('product_variant_count', '>', 1)]}"

	random_string = fields.Char(
		string=_("Random String"),
		compute="_compute_random_string",
		inverse="_set_random_string",
	)

	@api.depends("product_variant_ids", "product_variant_ids.random_string")
	def _compute_random_string(self):

		unique_variants = self.filtered(
			lambda temp: len(template.product_variant_ids) == 1
		)
		for temp in unique_variants:
			temp.random_string = temp.product_variant_ids.random_string

	def _set_random_string(self):
		for temp in self:
			if len(temp.product_variant_ids) == 1:
				temp.product_variant_ids.random_string = temp.random_string

	def generate_random_string(self):

		str = "".join(
			random.choices(
				string.ascii_uppercase + string.digits + string.ascii_lowercase, k=5
			)
		)
		self.update({"random_string": str})


class Productvatiant(models.Model):
	_inherit = "product.product"

	random_string = fields.Char(readonly=True, string=_("Random String"))

	def generate_random_string(self):
		str = "".join(
			random.choices(
				string.ascii_uppercase + string.digits + string.ascii_lowercase, k=5
			)
		)
		self.update({"random_string": str})
