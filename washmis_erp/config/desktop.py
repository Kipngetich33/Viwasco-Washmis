from __future__ import unicode_literals
from frappe import _
import frappe

def get_data():
	return [
		{
			"module_name": "WaSHMIS ERP",
			"category": "Modules",
			"label": _("WaSHMIS ERP"),
			"color": "#1abc9c",
			"icon": "octicon octicon-file-submodule",
			"type": "module",
			"disable_after_onboard": 1,
			"description": "WaSHMIS ERP",
			"onboard_present": 1
		},
	]


		