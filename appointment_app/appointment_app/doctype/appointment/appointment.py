# Copyright (c) 2024, Hamza H. Alsaqaf and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Appointment(Document):
	def after_insert(self):
		self.add_to_appointment_queue()
	def add_to_appointment_queue(self):
		q= frappe.get_doc("Appointment Queue",{
			"date":self.date,
			"shift":self.shift,
			"clinic":self.clinic,
		})
		q.append("queue",{
			"appointment":self.name,
			"status":"pending"
		})
		q.save(ignore_permission=True)
		return len(q.queue)
