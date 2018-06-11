// Copyright (c) 2018, E$J Technologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Vehicle Income', {
	refresh: function(frm) {

	},
	date:function(frm){
	if(frm.doc.date){
	    frm.set_value('next_payment_date',frappe.datetime.add_days(frm.doc.date, 7) )
	}


	},
    vehicle: function (frm) {
        frappe.call({
          method: 'fleet.fleet_manager.doctype.vehicle_income.vehicle_income.get_due_date',
          args: {
            'vehicle': frm.doc.vehicle,
            'status': frm.doc.status,
          },
          callback: function (r) {
            if (!r.exc) {
              frappe.msgprint(__(r.message))
              if(!was_due_on){
                  frm.set_value('was_due_on', r.message)
              }

            }
          }

        })
    }
});
