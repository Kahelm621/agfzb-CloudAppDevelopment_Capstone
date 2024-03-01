from cloudant.client import Cloudant
from flask import Flask, jsonify, request, abort

# Add your Cloudant service credentials here
cloudant_username = "fe3a4d3f-7121-4c42-a808-4aaa7551a198-bluemix"
cloudant_api_key = "NcS6IMZjZjT08Af8w3YmDRZLJ2m-DSu1Z0pGzi6smud-"
cloudant_url = "https://fe3a4d3f-7121-4c42-a808-4aaa7551a198-bluemix.cloudantnosqldb.appdomain.cloud"

# Connect to Cloudant using the provided credentials
client = Cloudant.iam(cloudant_username, cloudant_api_key, connect=True, url=cloudant_url)

# Connect to the service instance
client.connect()

# Create a Cloudant session
session = client.session()
print('Databases:', client.all_dbs())

# Specify the database
db = client['reviews']

app = Flask(__name__)

@app.route('/api/get_reviews', methods=['GET'])
def get_reviews():
    dealership_id = request.args.get('id')

    # Check if "id" parameter is missing
    if dealership_id is None:
        return jsonify({"error": "Missing 'id' parameter in the URL"}), 400

    # Convert the "id" parameter to an integer (assuming "id" should be an integer)
    try:
        dealership_id = int(dealership_id)
    except ValueError:
        return jsonify({"error": "'id' parameter must be an integer"}), 400

    # Define the query based on the 'dealership' ID
    selector = {'dealership': dealership_id}

    # Execute the query using the query method
    result = db.get_query_result(selector)

    # Create a list to store the documents
    data_list = []

    # Iterate through the results and add documents to the list
    for doc in result:
        data_list.append(doc)

    # Return the data as JSON
    return jsonify(data_list)


@app.route('/api/post_review', methods=['POST'])
def post_review():
    if not request.json:
        abort(400, description='Invalid JSON data')
    
    # Extract review data from the request JSON
    review_data = request.json

    # Validate that the required fields are present in the review data
    required_fields = ['id', 'name', 'dealership', 'review', 'purchase', 'purchase_date', 'car_make', 'car_model', 'car_year']
    for field in required_fields:
        if field not in review_data:
            abort(400, description=f'Missing required field: {field}')

    try:
        # Save the review data as a new document in the Cloudant database
        doc_info = db.create_document(review_data)
        # Extracting doc_id and doc_rev from the returned tuple
        doc_id, doc_rev = doc_info
    except ValueError:
        abort(500, description='Failed to create document in the database')

    return jsonify({"message": "Review posted successfully", "id": doc_id, "rev": doc_rev}), 201

if __name__ == '__main__':
    app.run(debug=True)