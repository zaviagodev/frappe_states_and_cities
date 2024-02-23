# Copyright (c) 2024, Frappe Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document, bulk_insert

import ijson
from py_countries_states_cities_database import get_file_path



class City(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		city_name: DF.Data
		country: DF.Link
		state: DF.Link | None
	# end: auto-generated types
	pass

def import_cities():
	print("Importing Cities...")
	cities = []
	ijson_cities = ijson.items(open(get_file_path("cities.json"), encoding="utf-8"), "item")
	for city_dict in ijson_cities:
		city = frappe._dict(city_dict)
		cities.append(
			frappe.get_doc(
				doctype="City",
				name=f"{city.name}-{city.country_code}",
				city_name=city.name,
				state=f"{city.state_name}-{city.country_code}",
				country=city.country_name
			)
		)
	bulk_insert("City", cities, ignore_duplicates=True)