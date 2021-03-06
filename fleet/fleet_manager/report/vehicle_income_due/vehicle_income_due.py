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
		row = [advance.name, advance.vehicle,advance.owner, advance.date, advance.next_payment_date, advance.amount]
		data.append(row)

	return columns, data


def get_columns():
	return [
		{
			"label": _("Dues No"),
			"fieldname": "due_no",
			"fieldtype": "Link",
			"options": "Vehicle Income",
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
			"label": _("Lat Payment Date"),
			"fieldname": "last_payment_date",
			"fieldtype": "Date",
			"width": 120
		},
		{
			"label": _("Due On"),
			"fieldname": "next_payment_date",
			"fieldtype": "Date",
			"width": 120
		},
		{
			"label": _("Amount"),
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
	# if filters.get("next_payment_date"):
	# 	conditions += " and date<=%(next_payment_date)s"

	return conditions

def get_advances(filters):
	conditions = get_conditions(filters)
	return frappe.db.sql("""select name, vehicle, owner, date, next_payment_date, 
	    DATEDIFF(next_payment_date, date ) *1000 as amount from `tabVehicle Income`
		where age='Last' %s order by date ASC""" %
						 conditions, filters, as_dict=1)