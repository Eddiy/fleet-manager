# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import msgprint, _

def execute(filters=None):
	if not filters: filters = {}

	advances_list = get_advances(filters)
	columns = get_columns()

	if not advances_list:
		msgprint(_("No record found"))
		return columns, advances_list

	data = []
	for advance in advances_list:
		row = [advance.name, advance.vehicle, advance.owner, advance.service,
			   advance.service_date, advance.amount]
		data.append(row)

	return columns, data


def get_columns():
	return [
		{
			"label": _("Expense No"),
			"fieldname": "title",
			"fieldtype": "Link",
			"options": "Vehicle Expense",
			"width": 120
		},
		{
			"label": _("Vehicle"),
			"fieldname": "vehicle",
			"fieldtype": "Link",
			"options": "Vehicle",
			"width": 120
		},
		{
			"label": _("Owner"),
			"fieldname": "owner",
			"fieldtype": "Link",
			"options": "Customer",
			"width": 120
		},
		{
			"label": _("Service Item"),
			"fieldname": "service",
			"fieldtype": "Link",
			"options": "Service Item",
			"width": 120
		},
		{
			"label": _("Expense Date"),
			"fieldname": "service_date",
			"fieldtype": "Date",
			"width": 120
		},
		{
			"label": _("Expense Amount"),
			"fieldname": "amount",
			"fieldtype": "Currency",
			"width": 120
		}
	]

def get_conditions(filters):
	conditions = ""

	if filters.get("vehicle"):
		conditions += " and vehicle = %(vehicle)s"
	if filters.get("owner"):
		conditions += " and owner = %(owner)s"
	if filters.get("from_date"):
		conditions += " and service_date>=%(from_date)s"
	if filters.get("to_date"):
		conditions += " and service_date<=%(to_date)s"


	return conditions

def get_advances(filters):
	conditions = get_conditions(filters)
	return frappe.db.sql("""select name, vehicle, owner, service, service_date, amount
		from `tabVehicle Expense`
		where docstatus<2 %s order by service_date, name desc""" %
						 conditions, filters, as_dict=1)
