# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe

__version__ = '1.0.0alpha'


@frappe.whitelist(allow_guest=True)
def get_website_user_lang():
	return frappe.local.lang