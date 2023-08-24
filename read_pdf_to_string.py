import json
import requests
from pathlib import Path


# The name of a document type in Sensible, e.g., "tax_forms"
DOCUMENT_TYPE = "tax_forms1"
# The path to the PDF you'd like to extract from
DOCUMENT_PATH = Path("2020-TaxReturn.pdf")
# Your Sensible API key
SENSIBLE_API_KEY  = "3f0e7662e2fdcb6e975ddfbc1b8c641e471c448ace453e967a5db1606c3593207a37bdb627233d0d6da84a480e19ffa954c9806ea3b1b0005bfc71bfbcfacdd9"

# The path to save the output
OUTPUT_PATH = Path("response.json")

# The path to save the exception (if occurs)
ERROR_PATH = Path("exception.json")

headers = {
    'Authorization': 'Bearer {}'.format(SENSIBLE_API_KEY),
    'Content-Type': 'application/pdf'
}

URL ="https://api.sensible.so/v0/extract/{}".format(DOCUMENT_TYPE)

def api_call():
    
    with DOCUMENT_PATH.open('rb') as pdf_file:
        body = pdf_file.read()
        response = requests.request(
            "POST",
            URL,
            headers=headers,
            data=body
        )
    return response 
    

def extract_doc():
    
    response = api_call()
   
    try:
        response.raise_for_status()
    except requests.RequestException as e:
        print(e)
        
        with ERROR_PATH.open('w') as error_file:
           error_file.write(str(e))
    else:
        response_json = response.json()
        
        # Access the key-value pairs in the 'parsed document'
        parsed_document=response_json['parsed_document']
        name=parsed_document["name"]
        home_street_address=parsed_document["home_street_address"]
        home_city_zip_code=parsed_document["home_city_state_zipcode"]
        ssn=parsed_document["ssn"]
  
        print("Name:", name["value"])
        print("Street Address: ", home_street_address["value"])
        print("City and Zip-Code: ", home_city_zip_code["value"])
        print("Social security number: ", ssn["value"])
        
        # Save the JSON output for further analysis
        with OUTPUT_PATH.open('w') as json_file:
            json.dump(response_json, json_file, indent=2)


if __name__ == '__main__':
    extract_doc()