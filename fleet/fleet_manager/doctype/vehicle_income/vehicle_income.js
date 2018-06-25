// Copyright (c) 2018, E$J Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Vehicle Income', {
	refresh: function(frm) {

	},
	date:function(frm){
	if(frm.doc.date){
	    frm.set_value('next_payment_date',frappe.datetime.add_days(frm.doc.date, 7) )
	}


	}
});
