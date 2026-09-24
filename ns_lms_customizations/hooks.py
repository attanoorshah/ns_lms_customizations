app_name = "ns_lms_customizations"
app_title = "NS-LMS Customizations"
app_publisher = "Global Northstar"
app_description = "Custom app for lms.globalnorthstar.net"
app_email = "admin@globalnorthstar.net"
app_license = "mit"

fixtures = [
	{"dt": "Custom Field", "filters": [["dt", "in", ["User", "LMS Course"]]]},
	{"dt": "Client Script", "filters": [["dt", "=", "User"]]},
]

page_renderer = ["ns_lms_customizations.zoho.ZohoCreateUserRenderer"]

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "ns_lms_customizations",
# 		"logo": "/assets/ns_lms_customizations/logo.png",
# 		"title": "NS-LMS Customizations",
# 		"route": "/ns_lms_customizations",
# 		"has_permission": "ns_lms_customizations.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ns_lms_customizations/css/ns_lms_customizations.css"
# app_include_js = "/assets/ns_lms_customizations/js/ns_lms_customizations.js"

# include js, css files in header of web template
# web_include_css = "/assets/ns_lms_customizations/css/ns_lms_customizations.css"
# web_include_js = "/assets/ns_lms_customizations/js/ns_lms_customizations.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ns_lms_customizations/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "ns_lms_customizations/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "ns_lms_customizations.utils.jinja_methods",
# 	"filters": "ns_lms_customizations.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "ns_lms_customizations.install.before_install"
# after_install = "ns_lms_customizations.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ns_lms_customizations.uninstall.before_uninstall"
# after_uninstall = "ns_lms_customizations.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "ns_lms_customizations.utils.before_app_install"
# after_app_install = "ns_lms_customizations.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "ns_lms_customizations.utils.before_app_uninstall"
# after_app_uninstall = "ns_lms_customizations.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "ns_lms_customizations.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ns_lms_customizations.notifications.get_notification_config"

# Awesome Bar
# -----------
# Extra search results: list of dicts with label, description, route, index.
# route: ["List", "ToDo"], "/desk/docs/some/page", or "https://example.com"
# awesomebar_search = ["ns_lms_customizations.search.awesomebar_results"]

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ns_lms_customizations.tasks.all"
# 	],
# 	"daily": [
# 		"ns_lms_customizations.tasks.daily"
# 	],
# 	"hourly": [
# 		"ns_lms_customizations.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ns_lms_customizations.tasks.weekly"
# 	],
# 	"monthly": [
# 		"ns_lms_customizations.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "ns_lms_customizations.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "ns_lms_customizations.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ns_lms_customizations.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ns_lms_customizations.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["ns_lms_customizations.utils.before_request"]
# after_request = ["ns_lms_customizations.utils.after_request"]

# Job Events
# ----------
# before_job = ["ns_lms_customizations.utils.before_job"]
# after_job = ["ns_lms_customizations.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"ns_lms_customizations.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

