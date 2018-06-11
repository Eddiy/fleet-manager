// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Vehicle Income Due"] = {
//    "onload":function(frm){
//        frappe.msgprint(__("jjjj"))
//    },
	"filters": [
		{
			"fieldname":"vehicle",
			"label": __("Vehicle"),
			"fieldtype": "Link",
			"options": "Vehicle",
			"width": "80"
		},
		{
        	"fieldname":"owner",
        	"label": __("Owner"),
        	"fieldtype": "Link",
        	"options": "Customer"
        }

	]
};




