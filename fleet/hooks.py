# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "fleet"
app_title = "Fleet Manager"
app_publisher = "E$J Technologies"
app_description = "Application for Fleet Management"
app_icon = "octicon octicon-car"
app_color = "#70ABD3  "
app_email = "infor@enj.co.ke"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/fleet/css/fleet.css"
# app_include_js = "/assets/fleet/js/fleet.js"

# include js, css files in header of web template
# web_include_css = "/assets/fleet/css/fleet.css"
# web_include_js = "/assets/fleet/js/fleet.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "fleet.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "fleet.install.before_install"
# after_install = "fleet.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "fleet.notifications.get_notification_config"

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

doc_events = {
	"Vehicle Income": {
        "before_insert":
            "fleet.fleet_manager.hooks.doc_hooks.update_last"

	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"fleet.tasks.all"
# 	],
# 	"daily": [
# 		"fleet.tasks.daily"
# 	],
# 	"hourly": [
# 		"fleet.tasks.hourly"
# 	],
# 	"weekly": [
# 		"fleet.tasks.weekly"
# 	]
# 	"monthly": [
# 		"fleet.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "fleet.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "fleet.event.get_events"
# }
fixtures = [
    "Custom Field"]
