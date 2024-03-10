# Copyright (c) 2024, Hamza H. Alsaqaf and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Doctor(Document):
	pass
	def validate(self):
		#make it befor_insert
		self.set_full_name()
	def set_full_name(self):
		#handle if last name not presedent
		self.full_name=((self.first_name+" "+self.last_name) if self.last_name else self.first_name)