// Copyright (c) 2024, JayaPrakash J and contributors
// For license information, please see license.txt

frappe.query_reports["Average Event Rating"] = {
	"filters": [
		{
			"fieldname":"event",
			"label":"Event",
			"fieldtype":"Link",
			"options":"Public Event"
		}
	]
};
