import json
import base64

def create_postman_collection_from_file(file_path):
    # Read hrefs from file
    with open(file_path, 'r') as file:
        # Removing the "href": " part from each line and stripping extra spaces
        hrefs = [line.replace('"href": "', '').rstrip('",\n').strip() for line in file if line.strip()]

    # Postman collection structure
    postman_collection = {
        "info": {
            "name": "Collection from HREFs",
            "description": "Generated from outputs.txt",
            "_postman_id": "generated-id",
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
        },
        "item": []
    }

    # Headers to include in each request
    headers = [
        {"key": "Content-Type", "value": "application/json"},
        {"key": "Accept", "value": "application/json"}
    ]

    # Basic Authorization (username:password base64 encoded)
    username = "apiuser"
    password = "K4f8"
    encoded_credentials = base64.b64encode(f"{username}:{password}".encode()).decode()
    auth_header = {"key": "Authorization", "value": f"Basic {encoded_credentials}"}
    headers.append(auth_header)

    # Add each href as a GET request with headers
    for i, href in enumerate(hrefs):
        try:
            request_item = {
                "name": f"Request {i+1}",
                "request": {
                    "method": "GET",
                    "header": headers,
                    "url": {
                        "raw": href,
                        "protocol": href.split(':')[0],
                        "host": href.split('/')[2].split('.'),
                        "path": href.split('/')[3:]
                    }
                },
                "response": []
            }
            postman_collection["item"].append(request_item)
        except IndexError as e:
            print(f"Error processing URL '{href}': {e}")

    # Save the collection to a JSON file
    output_file = 'postman_collection.json'
    with open(output_file, 'w') as file:
        json.dump(postman_collection, file, indent=4)

    print(f"Postman collection created: {output_file}")

# Replace 'outputs.txt' with the path to your file
create_postman_collection_from_file('outputs.txt')

