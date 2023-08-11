import os
from flask import Flask, jsonify, request
from github_scraper import get_user_info, get_repository_info

app = Flask(_name_)

# Define the base URL for the API
base_url = "/api/v1"

@app.route(base_url + "/user/<username>", methods=["GET"])
def get_user(username):
    user_data = get_user_info(username)
    if user_data:
        return jsonify(user_data), 200
    else:
        return jsonify({"message": "User not found"}), 404

@app.route(base_url + "/repository/<repo_name>", methods=["GET"])
def get_repository(repo_name):
    repo_data = get_repository_info(repo_name)
    if repo_data:
        return jsonify(repo_data), 200
    else:
        return jsonify({"message": "Repository not found"}), 404

if _name_ == "_main_":
    # Get the port number from the environment variable, default to 5000 if not set
    port = int(os.environ.get("GITHUB_API_PORT", 5000))
    app.run(host="0.0.0.0", port=port)