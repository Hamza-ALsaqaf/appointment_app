# Copyright (c) 2024, Hamza H. Alsaqaf and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Appointment(Document):
	def after_insert(self):
		self.queue_number = self.add_to_appointment_queue()
		# attach csrf token + queue number as key and queue number as value
		frappe.cache().set_value(f"{frappe.session.sid}:queue_number", self.queue_number)
		self.save(ignore_permissions=True)
		self.send_confirmation_message()
	def add_to_appointment_queue(self):
		filters = {
			"date": self.date,
			"shift": self.shift,
			"clinic": self.clinic,
		}
		appointment_queue_exists = frappe.db.exists(
			"Appointment Queue",
			filters,
		)

		if appointment_queue_exists:
			q = frappe.get_doc("Appointment Queue", filters)
		else:
			q = frappe.new_doc("Appointment Queue")
			q.update(filters)
			q.save(ignore_permissions=True)

		q.append("queue", {"appointment": self.name, "status": "Pending"})
		q.save(ignore_permissions=True)

		return len(q.queue)
	
	
	def send_confirmation_message(self):
		shift_title = frappe.db.get_value("Schedule Shift", self.shift, "title")
		message = f"Hi {self.patient_name}, your appointment for {self.clinic} on {self.date} ({shift_title}) has been booked. Your queue number is {self.queue_number}."

		frappe.enqueue(
			"appointments_app.utils.send_message",
			body=message,
			from_=frappe.db.get_single_value(
				"Appointments Twilio Settings", "from_phone_number"
			),
			to=self.contact_number,
		)
