# Copyright (c) 2019, Dokos and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals, absolute_import
import frappe
import datetime
from shared_place.shared_place.shared_place_connector import sync_accounts

def reset_draft_bookings():
	reset_period = frappe.db.get_value("Shared Place Settings", "Shared Place Settings", "booking_reset_period")
	if reset_period:
		comparison_datetime = datetime.datetime.now() - datetime.timedelta(minutes=int(reset_period))

		drafts = frappe.get_all("Quotation", filters=[['modified', '<=', comparison_datetime], ['docstatus', '=', 0], ['order_type', '=', 'Shopping Cart']])

		for draft in drafts:
			frappe.delete_doc("Quotation", draft.name, force=1)

def calendar_sync():
	try:
		gcalendar_settings = frappe.get_doc('GCalendar Settings')
		if gcalendar_settings.enable == 1:
			sync_accounts()
	except Exception:
		frappe.log_error(frappe.get_traceback())