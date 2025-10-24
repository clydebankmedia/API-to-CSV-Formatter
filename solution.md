# Solution Code - API to CSV Formatter

<details>
<summary> Step 1 Solution - Verify the Setup and Imports</summary>
Python - main.py    

```python
# STEP 1: Setup & Imports

# Import the libraries you'll need
import requests   # for making API calls
import csv        # for writing CSV files

# At this point, the script should run without errors.
# (No functional code needed yet.)
```

</details>


<details>
<summary>Step 2 Solution – Fetch and Explore Posts Data</summary>
Python - main.py

```python
# STEP 2: Fetch & Explore Posts Data
# (Inside main())

# Define the posts endpoint
url_posts = "https://jsonplaceholder.typicode.com/posts"

# Make a GET request
response_posts = requests.get(url_posts)

# Check that the request succeeded
print("Status code (posts):", response_posts.status_code)

# Convert response into Python data
posts = response_posts.json()

# Print the number of records
print("Number of posts:", len(posts))

# Print the first post to inspect structure for export
print("First post sample:", posts[0])
```
</details>  


<details>
<summary>Step 3 Solution – Normalize & Export Posts to CSV</summary>
Python - main.py

```python
# -------------------------------------
# STEP 3: Normalize & Export Posts to CSV
# (Inside main(), after Step 2)
# -------------------------------------

# Choose the headers you want for posts
post_headers = ["userId", "id", "title", "body"]

# Open a new CSV file for writing and export rows
with open("posts.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=post_headers)
    writer.writeheader()

    # Loop through each post and write one row
    for post in posts:
        writer.writerow(post)

print("posts.csv created with", len(posts), "rows")
```
</details>   


<details>
<summary> Step 4 Solution – Fetch and Explore Users Data</summary>
Python - main.py

```python
# STEP 4: Fetch & Explore Users Data
# (Inside main())

# Define the users endpoint
url_users = "https://jsonplaceholder.typicode.com/users"

# Make a GET request
response_users = requests.get(url_users)
users = response_users.json()

# Print how many users were returned
print("Number of users:", len(users))

# Print the first user record
print("First user sample:", users[0])
```
</details>   



<details>
<summary> Step 5 Solution – Normalize Users Data</summary>
Python - main.py

```python
# STEP 5: Normalize Users Data (Helper Function)
# (Defined outside main)

def normalize_users(users):
    """Flatten nested address and company data into a consistent structure."""
    normalized = []
    for user in users:
        # Flatten address into a single string
        address = f"{user['address']['street']}, {user['address']['suite']}, {user['address']['city']} {user['address']['zipcode']}"
        # Keep company name only
        company = user["company"]["name"]

        # Build flat record
        record = {
            "id": user["id"],
            "name": user["name"],
            "email": user["email"],
            "address": address,
            "company": company
        }
        normalized.append(record)
    return normalized

# Inside main(), after fetching users:
user_headers = ["id", "name", "email", "address", "company"]
normalized_users = normalize_users(users)

# Preview one normalized record for verification
print("First normalized user:", normalized_users[0])

```
</details>   



<details>
<summary> Step 6 Solution – Export Users Data to CSV</summary>
Python - main.py

```python
# STEP 6: Export to CSV (Reusable Helper)
# (Defined outside main)

def export_to_csv(data, headers, filename):
    """Write any list of dictionaries to a CSV file."""
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        print(f"{filename} created with {len(data)} rows.")
    except Exception as e:
        print("Error writing CSV:", e)

# Inside main(), after normalization:
export_to_csv(normalized_users, user_headers, "users.csv")
```
</details>   


<details>
<summary>Final Solution</summary>
Python - main.py

```python
# main.py — JSON to CSV Export Tool
# -------------------------------------
# This script fetches data from JSONPlaceholder and exports it into clean CSV files.
# Follow the project steps to gradually implement and refine your solution.

# -------------------------------------
# STEP 1: Setup & Imports
# -------------------------------------
import requests   # for making API calls
import csv        # for writing CSV files

# At this point, the script should run without errors.
# Run: python main.py

# -------------------------------------
# STEP 5: Normalize Users Data (Helper Function)
# -------------------------------------
def normalize_users(users):
    """Flatten nested address and company data into a consistent structure."""
    normalized = []
    for user in users:
        # Flatten address into a single string
        address = f"{user['address']['street']}, {user['address']['suite']}, {user['address']['city']} {user['address']['zipcode']}"
        # Keep company name only
        company = user["company"]["name"]

        # Build flat record
        row = {
            "id": user["id"],
            "name": user["name"],
            "email": user["email"],
            "address": address,
            "company": company,
        }
        normalized.append(row)
    return normalized

# -------------------------------------
# STEP 6: Export to CSV (Reusable Helper)
# -------------------------------------
def export_to_csv(data, headers, filename):
    """Write any list of dictionaries to a CSV file."""
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        print(f"{filename} created with {len(data)} rows.")
    except Exception as e:
        print("Error writing CSV:", e)

# -------------------------------------
# MAIN PROGRAM FUNCTION
# -------------------------------------
def main():
    """
    The main() function is the program's entry point.
    Each project step builds on the last inside this function.
    """

    print("JSON to CSV Export Tool initialized.")
    print("(Follow the project steps to implement functionality.)\n")

    # -------------------------------------
    # STEP 2: Fetch & Explore Posts Data
    # -------------------------------------
    url_posts = "https://jsonplaceholder.typicode.com/posts"
    response_posts = requests.get(url_posts)
    print("Status code (posts):", response_posts.status_code)
    posts = response_posts.json()
    print("Number of posts:", len(posts))
    print("First post sample:", posts[0])

    # -------------------------------------
    # STEP 3: Normalize & Export Posts to CSV
    # -------------------------------------
    post_headers = ["userId", "id", "title", "body"]

    # NOTE: Original inline Step 3 code is retained below for reference.
    # It has been replaced by the modular export helper after Step 6.
    #
    # with open("posts.csv", "w", newline="", encoding="utf-8") as file:
    #     writer = csv.DictWriter(file, fieldnames=post_headers)
    #     writer.writeheader()
    #     for post in posts:
    #         row = {
    #             "userId": post["userId"],
    #             "id": post["id"],
    #             "title": post["title"],
    #             "body": post["body"],
    #         }
    #         writer.writerow(row)
    # print("posts.csv created with", len(posts), "rows")

    # Export using the reusable helper
    export_to_csv(posts, post_headers, "posts.csv")

    # -------------------------------------
    # STEP 4: Fetch & Explore Users Data
    # -------------------------------------
    url_users = "https://jsonplaceholder.typicode.com/users"
    response_users = requests.get(url_users)
    users = response_users.json()
    print("Number of users:", len(users))
    print("First user sample:", users[0])

    # -------------------------------------
    # STEP 5: Normalize Users Data
    # -------------------------------------
    user_headers = ["id", "name", "email", "address", "company"]
    normalized_users = normalize_users(users)
    print("First normalized user:", normalized_users[0])

    # -------------------------------------
    # STEP 6: Export Users to CSV
    # -------------------------------------
    export_to_csv(normalized_users, user_headers, "users.csv")

    print("\n All exports complete.")

# -------------------------------------
# MAIN EXECUTION ENTRY POINT
# -------------------------------------
if __name__ == "__main__":
    main()

```
</details>