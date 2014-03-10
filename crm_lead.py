from openerp.addons.base_status.base_stage import base_stage
import crm
from datetime import datetime
from operator import itemgetter
from openerp.osv import fields, osv, orm
import time
from openerp import SUPERUSER_ID
from openerp import tools
from openerp.tools.translate import _
from openerp.tools import html2plaintext

from base.res.res_partner import format_address

class crm_lead(base_stage, format_address, osv.osv):
	""" CRM Lead Case """
	_name = "crm.lead"
	_inherit = "crm.lead"
	_columns = {

				'itsalutation': fields.many2one('res.partner.title', 'IT Salutation'),
				'itfirstname':fields.char('IT Firstname', size=64, required=True, select=1),
				'itsurname':fields.char('IT Surname', size=64, required=True, select=1),
				'itjobtitle':fields.char('IT Job Title', size=64, required=True, select=1),
				'itemail' :fields.char('IT Email', size=200, required=True, select=1),
				'sic_2003':fields.char('IT Firstname', size=64, required=True, select=1),
				'business':fields.text('Business'),
				'reg_no':fields.char('Registration Number', size=64, required=True, select=1),
				'holding_company':fields.char('Holding Company', size=200, required=True, select=1),
				'holding_country': fields.many2one('res.country', 'Holding Country'),
				'turnover':fields.char('Turn Over', size=64, required=True, select=1),
				'pretaxprofit':fields.char('Pre Tax Profit', size=64, required=True, select=1),
				'employees':fields.char('No of Employees', size=10, required=True, select=1),
				'mdemail' :fields.char('MD Email', size=200, required=True, select=1),
				'mdsurname':fields.char('MD Surname', size=64, required=True, select=1),
				'mdjobtitle':fields.char('MD Job Title', size=64, required=True, select=1)
	}

crm_lead()
