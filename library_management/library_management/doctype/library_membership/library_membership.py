# Copyright (c) 2025, Satria Faestha and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class LibraryMembership(Document):
	# check before submitting this document
  def before_submit(self):
    exists = frappe.db.exists(
      "Library Membership",
			{
				"library_member": self.library_member,
				"docstatus": DocStatus.submitted(),
        # check if the membership's end date is later than this membership's start date
				"to_date": [">", self.from_date],
			}
		)
    if exists:
      frappe.throw(f"The membership's end date ({self.to_date}) should be later than this membership's start date ({self.from_date}) for this member")
