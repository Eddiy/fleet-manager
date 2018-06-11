# -*- coding: utf-8 -*-
# Copyright (c) 2018, E$J Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class VehicleIncome(Document):
	pass

@frappe.whitelist()
def get_due_date(vehicle, status):
	due_date = frappe.db.get_value("Vehicle Income", {"vehicle":vehicle, "status": "Last"},
								   "next_payment_date")

	return due_date