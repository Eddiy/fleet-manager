from __future__ import unicode_literals

from frappe import _


def get_data():
    return [
        {
            "label": _("Documents"),
            "icon": "icon-star",
            "items": [
                {
                    "type": "doctype",
                    "name": "Vehicle",
                    "description": _("Vehicles database.")
                },
                {
                    "type": "doctype",
                    "name": "Vehicle Expense",
                    "description": _("Vehicle Expense database.")
                },
                {
                    "type": "doctype",
                    "name": "Vehicle Income",
                    "description": _("Vehicle Income details.")
                },
            ]
        },
        {
            "label": _("Setup"),
            "icon": "fa fa-list",
            "items": [
                {
                    "type": "doctype",
                    "name": "Service Items",
                    "description": _("Vehicle Service details.")
                },


            ]
        },
        {
            "label": _("Reports"),
            "icon": "fa fa-list",
            "items": [
                {
                    "type": "report",
                    "is_query_report": True,
                    "name": "Vehicle Expense Report",
                    "doctype": "Vehicle Expense"
                },
                {
                    "type": "report",
                    "is_query_report": True,
                    "name": "Vehicle Income Summary",
                    "doctype": "Vehicle Income"
                },
                {
                    "type": "report",
                    "is_query_report": True,
                    "name": "Vehicle Income Due",
                    "doctype": "Vehicle Income"
                }



            ]
        }
    ]
