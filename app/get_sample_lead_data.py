import json
import csv
from sample_lead_data import lead_data
from flask import url_for

def generate_lead_data(custom_field_ids):

	# Retrieve custom field IDs that were generated in the org
	custom_field_id_source = custom_field_ids[0]
	custom_field_id_industry = custom_field_ids[1]
	custom_field_id_lead_type = custom_field_ids[2]

	# Build the lead list so it includes the custom field IDs
	generated_lead_data = []

	for lead in lead_data:

		try:
			generated_lead_data.append(
				{
				    "lead_status": lead['lead_status'],
				    "name": lead['name'],
				    custom_field_id_industry: lead['CUSTOM_FIELD_LEAD_INDUSTRY'],
				    "addresses": [
					      {
					        "city": lead['addresses'][0]['city'],
					        "state": lead['addresses'][0]['state'],
					        "zip_code": lead['addresses'][0]['zip_code']
					      }
				    ],
				    "contacts": [
				      {
				        "phones": [
				          {
				            "phone": lead['contacts'][0]['phones'][0]['phone'],
				            "type": lead['contacts'][0]['phones'][0]['type']
				          }
				        ],
				        "name": lead['contacts'][0]['name'],
				        "emails": [
				          {
				            "type": lead['contacts'][0]['emails'][0]['type'],
				            "email": lead['contacts'][0]['emails'][0]['email']
				          }
				        ],
				        "title": lead['contacts'][0]['title']
				      }
				    ],
				    custom_field_id_source: "Sample Lead Importer",
				    custom_field_id_lead_type: lead['CUSTOM_FIELD_LEAD_TYPE'],
				    "description": lead['description']
				  }
			)
		except KeyError:
			generated_lead_data.append(
				{
				    "lead_status": lead['lead_status'],
				    "name": lead['name'],
				    custom_field_id_industry: lead['CUSTOM_FIELD_LEAD_INDUSTRY'],
				    "addresses": [
					      {
					        "city": lead['addresses'][0]['city'],
					        "state": lead['addresses'][0]['state'],
					        "zip_code": lead['addresses'][0]['zip_code']
					      }
				    ],
				    "contacts": [
				      {
				        "name": lead['contacts'][0]['name'],
				        "title": lead['contacts'][0]['title']
				      }
				    ],
				    custom_field_id_source: "Sample Lead Importer",
				    custom_field_id_lead_type: lead['CUSTOM_FIELD_LEAD_TYPE'],
				    "description": lead['description']
				  }
			)

	return generated_lead_data


