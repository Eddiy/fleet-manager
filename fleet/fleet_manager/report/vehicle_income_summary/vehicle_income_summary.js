// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Vehicle Income Summary"] = {
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
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.defaults.get_user_default("year_start_date"),
			"width": "80"
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default":frappe.datetime.add_days(frappe.datetime.get_today(), 2)
		},
		{
			"fieldname":"owner",
			"label": __("Owner"),
			"fieldtype": "Link",
			"options": "Customer"
		},
		{
			"fieldname":"status",
			"label": __("Status"),
			"fieldtype": "Select",
			"options": "\nPaid\nUnpaid",
			"default":"Paid"
		}
	],
	"formatter":function (row, cell, value, columnDef, dataContext, default_formatter) {
        value = default_formatter(row, cell, value, columnDef, dataContext);
        if (columnDef.id == "Amount")
            {
                if(dataContext.amount>"7000")
                    {
                        value = "<span style='color:green!important;font-weight:bold;'>" + value + "</span>";
                    }
                else if(dataContext.amount<"7000"){
                    value = "<span style='color:red!important;font-weight:bold;'>" + value + "</span>";
                }

            }
        return value;
    }

};




