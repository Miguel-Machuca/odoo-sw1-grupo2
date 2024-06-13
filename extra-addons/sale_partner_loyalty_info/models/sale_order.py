from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"


    order_points = fields.Float(
        string="Loyalty Points",
        compute="_get_loyalty_points",
        store=True,
        help="Partner Loyalty Points earned"
    )

    @api.depends("amount_total", "coupon_point_ids")
    def _get_loyalty_points(self):
        for sale in self:
            if sale.coupon_point_ids:
                points = sale.coupon_point_ids.mapped("points")
                sale.order_points = sum(points)
                print(f"Order points recomputed: >>>> {points}")
            else:
                sale.order_points = 0.0