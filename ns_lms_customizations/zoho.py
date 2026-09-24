import json

import frappe
from werkzeug.wrappers import Response


class ZohoCreateUserRenderer:
	def __init__(self, path, http_status_code=None):
		self.path = path
		self.http_status_code = http_status_code

	def can_render(self):
		return self.path == "zoho/create-user"

	def render(self):
		try:
			result = create_user_from_zoho(frappe.local.request.args)
			status = 200
		except frappe.PermissionError:
			result, status = {"error": "Invalid or missing token"}, 403
		except frappe.DuplicateEntryError as e:
			result, status = {"error": str(e)}, 409
		except frappe.ValidationError as e:
			result, status = {"error": str(e)}, 400
		except Exception:
			frappe.db.rollback()
			frappe.log_error(title="Zoho create-user webhook error")
			result, status = {"error": "Internal server error"}, 500
		return Response(json.dumps(result), status=status, mimetype="application/json")


def create_user_from_zoho(args):
	expected = frappe.conf.get("zoho_webhook_token")
	if not expected or args.get("token") != expected:
		frappe.throw("Invalid token", frappe.PermissionError)

	email = (args.get("email") or "").strip()
	if not email:
		frappe.throw("Missing email", frappe.ValidationError)
	if frappe.db.exists("User", email):
		frappe.throw(f"User {email} already exists", frappe.DuplicateEntryError)

	first_name = (args.get("first") or "").strip() or email
	last_name = (args.get("last") or "").strip()
	# contactId is accepted but not persisted in this first version — easy to
	# add a dedicated field later if it needs to be tracked on the User.

	user = frappe.get_doc(
		{
			"doctype": "User",
			"email": email,
			"first_name": first_name,
			"last_name": last_name,
			"send_welcome_email": 1,
		}
	)
	user.append("roles", {"role": "LMS Student"})
	user.insert(ignore_permissions=True)
	frappe.db.commit()

	return {"success": True, "user": user.name}
