# import requests

# url = "https://api.sandbox.africastalking.com/version1/messaging"

# headers = {'ApiKey': 'c110a50034b61d4deb579bd45053013a9a647d896106c5d617ea986f2e6a565d', 
#            'Content-Type': 'application/x-www-form-urlencoded',
#            'Accept': 'application/json'}

# data = {'username': 'sandbox',
#         'from': '24412',
#         'message': "Hello world !",
#         'to': '+254726869778'}


# def make_post_request():  
#     response = requests.post( url = url, headers = headers, data = data )
#     return response


# print( make_post_request().json() )


#import package
import africastalking


# Initialize SDK
username = "sandbox"    # use 'sandbox' for development in the test environment
api_key = "c110a50034b61d4deb579bd45053013a9a647d896106c5d617ea986f2e6a565d"      # use your sandbox app API key for development in the test environment
africastalking.initialize(username, api_key)


# Initialize a service e.g. SMS
sms = africastalking.SMS


# Use the service synchronously
response = sms.send("Hello Munaa!", ["+254726869778"])

# # Or use it asynchronously
# def on_finish(error, response):
#     if error is not None:
#         raise error
#     print(response)

# sms.send("Hello Message!", ["254726869778"], callback=on_finish)