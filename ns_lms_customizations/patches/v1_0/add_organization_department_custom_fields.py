import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

CLIENT_SCRIPT_NAME = "ns_user_organization_department_filter"

CLIENT_SCRIPT = """frappe.ui.form.on("User", {
	refresh(frm) {
		frm.set_query("ns_department", () => ({
			filters: { organization: frm.doc.ns_organization || "" },
		}));
	},
	ns_organization(frm) {
		frm.set_value("ns_department", "");
		frm.set_query("ns_department", () => ({
			filters: { organization: frm.doc.ns_organization || "" },
		}));
	},
});
"""


def get_custom_fields():
	return {
		"User": [
			{
				"fieldname": "ns_organization_section",
				"fieldtype": "Section Break",
				"label": "Organization Details",
				"insert_after": "follow_assigned_documents",
				"collapsible": 1,
			},
			{
				"fieldname": "ns_organization",
				"fieldtype": "Link",
				"label": "Organization",
				"options": "Organization",
				"insert_after": "ns_organization_section",
				"in_standard_filter": 1,
			},
			{
				"fieldname": "ns_column_break_org",
				"fieldtype": "Column Break",
				"insert_after": "ns_organization",
			},
			{
				"fieldname": "ns_department",
				"fieldtype": "Link",
				"label": "Department",
				"options": "Department",
				"insert_after": "ns_column_break_org",
				"depends_on": "eval:doc.ns_organization",
			},
		],
		"LMS Course": [
			{
				"fieldname": "ns_organization",
				"fieldtype": "Link",
				"label": "Organization",
				"options": "Organization",
				"insert_after": "category",
				"in_standard_filter": 1,
			},
		],
	}


def create_or_update_department_filter_script():
	if frappe.db.exists("Client Script", CLIENT_SCRIPT_NAME):
		doc = frappe.get_doc("Client Script", CLIENT_SCRIPT_NAME)
		doc.script = CLIENT_SCRIPT
		doc.enabled = 1
		doc.save(ignore_permissions=True)
	else:
		frappe.get_doc(
			{
				"doctype": "Client Script",
				"name": CLIENT_SCRIPT_NAME,
				"dt": "User",
				"view": "Form",
				"module": "NS-LMS Customizations",
				"enabled": 1,
				"script": CLIENT_SCRIPT,
			}
		).insert(ignore_permissions=True)


def execute():
	create_custom_fields(get_custom_fields(), update=True)
	create_or_update_department_filter_script()
