# Copyright (c) 2024, Hamza H. Alsaqaf and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.utils import format_time
class ScheduleShift(Document):
	def before_save(self):
		self.title=(
			
					format_time(self.start_time,"HH:mm")+"-"+format_time(self.end_time,"HH:mm")
			
			)
