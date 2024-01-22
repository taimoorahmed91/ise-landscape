import json

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

    # Add each href as a GET request
    for i, href in enumerate(hrefs):
        try:
            request_item = {
                "name": f"Request {i+1}",
                "request": {
                    "method": "GET",
                    "header": [],
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

