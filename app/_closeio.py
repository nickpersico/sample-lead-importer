from closeio_api import Client as CloseIO_API, APIError
from get_sample_lead_data import generate_lead_data
import json

def run_import(api_key, list_type):

	import_status = ''
	api = CloseIO_API(api_key)

	# Try API Key
	try:
		test_api_key = api.get('me')
	except:
		import_status = 'bad_api_key'
		return import_status

	### Get Close.io Custom Fields
	print "...Getting Current Custom Fields"
	current_custom_fields = {}
	has_more = True
	offset = 0

	while has_more:
		resp = api.get('custom_fields/lead', params={ '_skip': offset, '_fields': 'id,name' })
		for field in resp['data']:
			current_custom_fields[field['name']] = field['id']
		offset += len(resp['data'])
		has_more = resp['has_more']

	### Create Custom Fields
	print "...Creating Any Missing Custom Fields"

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
		if custom_field['name'] in current_custom_fields:
			custom_field_ids.append("custom.{}".format(current_custom_fields[custom_field['name']]))
		else:
			try:
				create_custom_field = api.post('custom_fields/lead', data=custom_field)
				custom_field_ids.append("custom.{}".format(create_custom_field['id']))
				print "... {} Custom Field added".format(custom_field['name'])
			except:
				import_status = 'custom_field_error'
				return import_status
				break

	### Import Sample Leads
	print "... Creating Sample Leads"
	sample_lead_data = generate_lead_data(custom_field_ids=custom_field_ids, list_type=list_type)

	for lead in sample_lead_data:
		try:
			lead = api.post('lead', data=lead)
			print "... Importing {}".format(lead['name'])
		except:
			continue

	### Get Current Close.io Smart views
	print "...Getting Current Smart Views"
	current_smart_views = {}
	has_more = True
	offset = 0

	while has_more:
		resp = api.get('saved_search', params={ '_skip': offset, '_fields': 'id,name' })
		for query in resp['data']:
			current_smart_views[query['name']] = query['id']
		offset += len(resp['data'])
		has_more = resp['has_more']
		
	### Create Smart Views
	print "...Creating Any Missing Smart Views"
	smart_view_queries = [
		{
			'name': '[SAMPLE] {} Leads w/ Phone and Email'.format(list_type),
			'query': '"custom.Lead Source (Sample)":"Sample Lead Importer" "custom.List Type (Sample)":"{}" has:phone_numbers has:email_addresses sort:display_name'.format(list_type)
		},
		{
			'name': '[SAMPLE] {} Sample Leads'.format(list_type),
			'query': '"custom.Lead Source (Sample)":"Sample Lead Importer" "custom.List Type (Sample)":"{}" sort:display_name'.format(list_type)
		}
	]

	for query in smart_view_queries:
		if query['name'] not in current_smart_views:
			try:
				create_smart_view = api.post('saved_search', data=query)
				print "... {} Smart View added".format(query['name'])
			except:
				import_status = 'smartview_create_error'
				return import_status
				break

	import_status = 'https://app.close.io/search/%22custom.Lead%20Source%20(Sample)%22%3A%22Sample%20Lead%20Importer%22%20has%3Aphone_numbers%20has%3Aemail_addresses/'

	return import_status
