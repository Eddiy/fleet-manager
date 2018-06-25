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

	],
	"formatter":function (row, cell, value, columnDef, dataContext, default_formatter) {
            value = default_formatter(row, cell, value, columnDef, dataContext);
            var date=new Date(dataContext.next_payment_date);
//            var parts =dataContext.due_on.split('-');
//            var mydate = new Date(parts[0], parts[1] - 1, parts[2]);
//            frappe.msgprint(__(mydate))
//            var date=new Date(dataContext.due_on);
//            var today=new Date()
//              var tom= frappe.datetime.add_days(frappe.datetime.get_today(), 7)
//              var diff=frappe.datetime.get_day_diff(tom, frappe.datetime.get_today())
//              frappe.msgprint(__(frappe.datetime.get_day_diff(tom, frappe.datetime.get_today())))
//              frappe.msgprint(__(frappe.datetime.get_day_diff(dataContext.next_payment_date, frappe.datetime.get_today())))


            var date1 = new Date(frappe.datetime.get_today());
            var date2 = new Date(dataContext.next_payment_date);
            var diffDays = parseInt((date2 - date1) / (1000 * 60 * 60 * 24));

            if (columnDef.id == "Amount" || columnDef.id != "Amount")
                {
                    if(diffDays<0){
                        value = "<span style='color:red!important;font-weight:bold;'>" + value + "</span>";
                    }
                    else if(diffDays==0){
                        value = "<span style='color:green!important;font-weight:bold;'>" + value + "</span>";

                    }


                }
            return value;
        }
};




