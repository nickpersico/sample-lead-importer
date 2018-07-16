from closeio_api import Client as CloseIO_API
import json

def run_import(email, api_key, list_type):

	### Create a Smart View
	new_custom_field = {
    	"name": "Lead Source",
    	"type": "text"
	}

	api = CloseIO_API(api_key)
	create_custom_field = api.post('custom_fields/lead', data=new_custom_field)
	custom_field_id = "custom.{}".format(create_custom_field['id'])
	print custom_field_id

	### Sample Lead
	sample_lead_data = {
		"name": "Sample Lead Importer Test Lead 1",
		"contacts": [
		        {
		            "name": "Phone Number Test 1",
		            "title": "Sr. Vice President",
		            "emails": [
		                {
		                    "type": "office",
		                    "email": "nicklpersico+samplelead@gmail.com"
		                }
		            ],
		            "phones": [
		                {
		                    "type": "office",
		                    "phone": "+17045869022"
		                }
		            ]
		        }
		    ],
		"lead_status": "Potential",
		"description": "Test Lead",
		custom_field_id: "Sample Lead Importer"
	}

	api = CloseIO_API(api_key)
	lead = api.post('lead', data=sample_lead_data)

	### Create a Smart View
	new_smart_view = {
    	"name": "Test the Power Dialer!",
    	"query": """custom.Lead Source":"Sample Lead Importer"""
	}

	api = CloseIO_API(api_key)
	create_smart_view = api.post('saved_search', data=new_smart_view)

	return "https://app.close.io/search/custom.Lead%20Source%22%3A%22Sample%20Lead%20Importer/"