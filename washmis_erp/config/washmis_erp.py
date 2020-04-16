from __future__ import unicode_literals
from frappe import _
import frappe


def get_data():
	return [
		{
			"label": _("Customer"),
			"items": [
				{
					"type": "doctype",
					"name": "Account Registration",
					"description": _("Account Registration"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Customer Type",
					"description": _("Customer Type"),
					"onboard": 1,
				},
                {
					"type": "doctype",
					"name": "Customer System Number",
					"description": _("Customer System Number"),
					"onboard": 1,
				},
            ]
        },
        {
			"label": _("Survey"),
			"items": [
				{
					"type": "doctype",
					"name": "Survey Data",
					"description": _("Survey Data"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "GIS Data",
					"description": _("GIS Data"),
					"onboard": 1,
				},
                {
					"type": "doctype",
					"name": "Meter Map Location",
					"description": _("Meter Map Location"),
					"onboard": 1,
				},
            ]
        },
        {
			"label": _("Meter Reading"),
			"items": [
				{
					"type": "doctype",
					"name": "Reading Sheet",
					"description": _("Reading Sheet"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Meter Reading Capture",
					"description": _("Meter Reading Capture"),
					"onboard": 1,
				},
                {
					"type": "doctype",
					"name": "Capture Bulk Meter Readings",
					"description": _("Capture Bulk Meter Readings"),
					"onboard": 1,
				},
                {
					"type": "doctype",
					"name": "Meter Readings Adjustment",
					"description": _("Meter Readings Adjustment"),
					"onboard": 1,
				},
                {
					"type": "doctype",
					"name": "Consumption Adjustment Capture",
					"description": _("Consumption Adjustment Capture"),
					"onboard": 1,
				},
            ]
        },
        {
			"label": _("Non Revenue Water"),
			"items": [
				{
					"type": "doctype",
					"name": "Non Revenue Capture",
					"description": _("Non Revenue Capture"),
					"onboard": 1,
				}
            ]
        },
        {
			"label": _("More"),
			"items": [
				{
					"type": "doctype",
					"name": "Billing Period",
					"description": _("Billing Period"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Disconnection Profile",
					"description": _("Disconnection Profile"),
					"onboard": 1,
				},
                {
					"type": "doctype",
					"name": "System Values",
					"description": _("System Values"),
					"onboard": 1,
				},
                {
					"type": "doctype",
					"name": "Disconnection Mode",
					"description": _("Disconnection Mode"),
					"onboard": 1,
				},
                {
					"type": "doctype",
					"name": "Reading Code",
					"description": _("Reading Code"),
					"onboard": 1,
				},
            ]
        },
    ]

