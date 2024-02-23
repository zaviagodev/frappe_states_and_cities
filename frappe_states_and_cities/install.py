from frappe_states_and_cities.frappe_states_and_cities.doctype.state.state import import_states
from frappe_states_and_cities.frappe_states_and_cities.doctype.city.city import import_cities

def after_install():
    import_states()
    import_cities()