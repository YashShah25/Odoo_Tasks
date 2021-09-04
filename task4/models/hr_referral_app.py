from odoo import fields, models
from odoo.tools.translate import _


class HrReferral(models.Model):
    _name = "hr.referral"
    _description = "HR Reference Model"

    name = fields.Char(string=_("Name", required=True))
    email = fields.Char(string=_("Email"))
    referral_name = fields.Many2one("hr.employee", string=_("Referral Name"))
    # many2one(with hr.employee)
    degree = fields.Many2one("hr.recruitment.degree", string=_("Degree"))
    # many2one(with hr.recruitment.degree)
    department = fields.Many2one("hr.job", string=_("Department"))
    # many2one(with hr.job)
    expected_salary = fields.Integer(string=_("Expected Salary"))
    summary = fields.Text(string=_("Summary"))
    expected_joining_date = fields.Date(string=_("Expected Joining Date"))
    state = fields.Selection(
        [("draft", "Draft"), ("confirm", "Approved"), ("cancel", "Cancel")],
        default="draft",
    )

    def action_confirm(self):
        for rec in self:
            rec.state = "confirm"

    def action_cancel(self):
        for rec in self:
            rec.state = "cancel"
