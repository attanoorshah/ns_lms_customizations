import frappe
from werkzeug.wrappers import Response

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
	body {{ font-family: -apple-system, Segoe UI, Roboto, Arial, sans-serif;
		display: flex; align-items: center; justify-content: center;
		min-height: 100vh; margin: 0; background: #f5f6f8; color: #1f2328; }}
	.card {{ background: #fff; border-radius: 10px; padding: 2.5rem 3rem;
		box-shadow: 0 1px 3px rgba(0,0,0,.1); text-align: center; max-width: 420px; }}
	.icon {{ font-size: 2.5rem; margin-bottom: .75rem; }}
	h1 {{ font-size: 1.15rem; margin: 0 0 .4rem; }}
	p {{ color: #57606a; margin: 0; font-size: .95rem; }}
</style>
</head>
<body>
	<div class="card">
		<div class="icon">{icon}</div>
		<h1>{title}</h1>
		<p>{message}</p>
	</div>
</body>
</html>"""


def page(title, message, icon, status):
	return Response(PAGE.format(title=title, message=message, icon=icon), status=status, mimetype="text/html")


class ZohoCreateUserRenderer:
	def __init__(self, path, http_status_code=None):
		self.path = path
		self.http_status_code = http_status_code

	def can_render(self):
		return self.path == "zoho/create-user"

	def render(self):
		try:
			email = create_user_from_zoho(frappe.local.request.args)
			return page("User created", f"{email} has been added to the LMS.", "✅", 200)
		except frappe.PermissionError:
			return page("Not authorized", "This link is not valid.", "⛔", 403)
		except frappe.DuplicateEntryError:
			return page("Already exists", "This email or user already exists.", "⚠️", 409)
		except frappe.ValidationError as e:
			return page("Missing information", str(e), "⚠️", 400)
		except Exception:
			frappe.db.rollback()
			frappe.log_error(title="Zoho create-user webhook error")
			return page("Something went wrong", "Please try again or contact support.", "❌", 500)


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

	return user.name
