# API help page: https://sheet.zoho.com/help/api/v2/

from requests import Session

# Replace with your API URL from API help page
apiUrl = 'https://sheet.zoho.com/api/v2/g64ai55c4adb23ba543e29a83bda5fb700c13'

# Replace with your access token generated from API help page
accessToken = 'Zoho-oauthtoken 1000.6ef92232bc6726a024acee8ca368d32d.5a5057b0cb98ebf173441c2a79fb3236'

# Replace with your request parameters from API help page
requestParameters = {
	'method'		: 'cell.content.set',
	'worksheet_name': 'Sheet1',
	'row'			: '1',
	'column'		: '1',
	'content'		: 'test'
}

response = Session().post(apiUrl, requestParameters, headers = {
	'Authorization': accessToken
})
if (response.status_code == 200):
	print("Success")
	# Uncomment the next line to print the response
	print(response.text)
else:
	print("Failed")
