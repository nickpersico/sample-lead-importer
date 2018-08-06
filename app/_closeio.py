from closeio_api import Client as CloseIO_API
from get_sample_lead_data import generate_lead_data
import json

def run_import(api_key):

	import_status = ''
	api = CloseIO_API(api_key)

	# Try API Key
	try:
		test_api_key = api.get('me')
	except:
		import_status = 'bad_api_key'
		return import_status


	### Create Custom Fields
	print "Creating Custom Fields"

	new_custom_fields = [
		{
    		"name": "Lead Source (Sample)",
    		"type": "text"
		},
		{
    		"name": "Industry (Sample)",
    		"type": "text"
		},
		{
			"name": "List Type (Sample)",
			"type": "text"
		}
	]

	custom_field_ids = []

	for custom_field in new_custom_fields:

		try:
			create_custom_field = api.post('custom_fields/lead', data=custom_field)
			custom_field_ids.append("custom.{}".format(create_custom_field['id']))
		except:
			import_status = 'custom_field_error'
			return import_status
			break

	### Import Sample Leads
	print "... Creating Sample Leads"
	sample_lead_data = generate_lead_data(custom_field_ids=custom_field_ids)

	for lead in sample_lead_data:
		try:
			lead = api.post('lead', data=lead)
			print "... Importing {}".format(lead['name'])
		except:
			continue

	### Create Smart Views
	print "... Creating Smart Views"
	smart_view_queries = [
		{
			'name': '[SAMPLE] B2B Test Calling & Email',
			'query': '"custom.Lead Source (Sample)":"Sample Lead Importer" "custom.List Type (Sample)":"B2B" has:phone_numbers has:email_addresses'
		},
		{
			'name': '[SAMPLE] B2C Test Calling & Email',
			'query': '"custom.Lead Source (Sample)":"Sample Lead Importer" "custom.List Type (Sample)":"B2C" has:phone_numbers has:email_addresses'
		},
		{
			'name': '[SAMPLE] B2B Sample Leads',
			'query': '"custom.Lead Source (Sample)":"Sample Lead Importer" "custom.List Type (Sample)":"B2B"'
		},
		{
			'name': '[SAMPLE] B2C Sample Leads',
			'query': '"custom.Lead Source (Sample)":"Sample Lead Importer" "custom.List Type (Sample)":"B2C"'
		}
	]

	for query in smart_view_queries:
		create_smart_view = api.post('saved_search', data=query)
		print "... {} Smart View added".format(query['name'])

	import_status = 'https://app.close.io/search/%22custom.Lead%20Source%20%28Sample%29%22%3A%22Sample%20Lead%20Importer%22'

	return import_status