import frappe
from frappe import _
from lms.lms.utils import can_modify_course
from pypika import functions as fn


@frappe.whitelist()
def get_course_enrollment_by_organization(course: str):
	"""Enrollment counts per Organization for a given LMS Course."""
	if not can_modify_course(course):
		frappe.throw(
			_("You do not have permission to access this course's enrollment data."),
			frappe.PermissionError,
		)

	Enrollment = frappe.qb.DocType("LMS Enrollment")
	User = frappe.qb.DocType("User")
	Organization = frappe.qb.DocType("Organization")

	rows = (
		frappe.qb.from_(Enrollment)
		.join(User)
		.on(Enrollment.member == User.name)
		.left_join(Organization)
		.on(User.ns_organization == Organization.name)
		.select(
			Organization.name.as_("organization"),
			Organization.organization_name.as_("organization_name"),
			fn.Count(Enrollment.name).as_("count"),
		)
		.where(Enrollment.course == course)
		.groupby(Organization.name)
		.run(as_dict=True)
	)

	for row in rows:
		row["organization_name"] = row["organization_name"] or _("Not Assigned")

	rows.sort(key=lambda r: r["count"], reverse=True)

	total = sum(row["count"] for row in rows) or 0
	for row in rows:
		row["percentage"] = round((row["count"] / total) * 100, 1) if total else 0

	return {"rows": rows, "total": total}


@frappe.whitelist()
def get_course_members_by_organization(course: str, organization: str | None = None):
	"""Enrolled members for one course, filtered to one Organization.

	`organization` falsy means the "Not Assigned" bucket (users with no
	ns_organization set), matching the sentinel used by
	get_course_enrollment_by_organization.
	"""
	if not can_modify_course(course):
		frappe.throw(
			_("You do not have permission to access this course's enrollment data."),
			frappe.PermissionError,
		)

	Enrollment = frappe.qb.DocType("LMS Enrollment")
	User = frappe.qb.DocType("User")

	query = (
		frappe.qb.from_(Enrollment)
		.join(User)
		.on(Enrollment.member == User.name)
		.select(
			Enrollment.member,
			Enrollment.member_name,
			Enrollment.member_image,
			Enrollment.progress,
		)
		.where(Enrollment.course == course)
	)
	if organization:
		query = query.where(User.ns_organization == organization)
	else:
		query = query.where((User.ns_organization.isnull()) | (User.ns_organization == ""))

	return query.orderby(Enrollment.member_name).run(as_dict=True)
