# Copyright (c) 2024, JayaPrakash J and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data

def get_columns():
	col = []
	col.append({
		"fieldname":"event",
		"label":"Event",
		"fieldtype":"Link",
		"options":"Public Event"
	})
	col.append({
		"fieldname":"count",
		"label":"Count",
		"fieldtype":"Int"
	})
	col.append({
		"fieldname":"rating",
		"label":"Rating",
		"fieldtype":"Rating"
	})
	return col
	
def get_data(filters):
	condition = ""
	if filters.get("event"):
		condition = "WHERE event = %(event)s"
	query = f"SELECT event, COUNT(rating), SUM(rating)/COUNT(rating) FROM `tabEvent Feedback` {condition} GROUP BY event"
	data = frappe.db.sql(query, filters)
	# output = []
	# data = frappe.db.get_all("Event Feedback", filters=filters, fields=["event", "rating"])
	return data