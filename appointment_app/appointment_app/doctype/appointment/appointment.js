// Copyright (c) 2024, Hamza H. Alsaqaf and contributors
// For license information, please see license.txt

frappe.ui.form.on('Appointment', {
	refresh: function(frm) {
		frm.set_query('shift', function (doc) {
			return {
				filters: {
					"clinic":doc.clinic
				}
			};
		});
	},
	onload:function(frm)
	{
		frm.set_query('shift', function (doc) {
			return {
				filters: {
					"clinic": doc.clinic,
				}
			};
		});
	}
});
