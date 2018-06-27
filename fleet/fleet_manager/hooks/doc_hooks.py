from __future__ import unicode_literals

import frappe
from frappe import _
from frappe.utils import nowdate




def update_last(doc, method):
    frappe.db.sql("""update `tabVehicle Income` set age='old' where vehicle=%s 
            and age=%s""",  (doc.vehicle, doc.age))

