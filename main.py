# main.py — JSON to CSV Export Tool
# -------------------------------------
# This script will fetch data from JSONPlaceholder and export it into CSV files.
# Follow each numbered STEP in the project instructions to build functionality.


# -------------------------------------
# STEP 1: Setup & Imports
# -------------------------------------
"""
Goal:
Verify that your environment works and import the libraries you’ll need in later steps.

Tasks:
- Import the 'requests' module for API calls
- Import the 'csv' module for file writing
- Run `python main.py` to confirm no errors
"""


# -------------------------------------
# STEP 2: Fetch & Explore Posts Data
# -------------------------------------
"""
Goal:
Fetch data from the JSONPlaceholder /posts endpoint and preview the dataset.

Tasks:
- Define the posts endpoint URL
- Make a GET request with requests.get()
- Print status code, record count, and one example record
"""


# -------------------------------------
# STEP 3: Normalize & Export Posts to CSV
# -------------------------------------
"""
Goal:
Convert post data into a clean, tabular format and write to 'posts.csv'.

Tasks:
- Choose headers: userId, id, title, body
- Use csv.DictWriter to create and populate the file
- Confirm correct headers and record count
"""


# -------------------------------------
# STEP 4: Fetch & Explore Users Data
# -------------------------------------
"""
Goal:
Fetch and inspect the more complex /users endpoint to understand nested data.

Tasks:
- Request JSONPlaceholder /users
- Print total users and one example user
- Identify which nested fields (address, company) will need flattening
"""


# -------------------------------------
# STEP 5: Normalize Users Data
# -------------------------------------
"""
Goal:
Flatten nested address and company fields into a consistent structure.

Tasks:
- Define a helper function normalize_users(users)
- Decide your schema (id, name, email, address, company)
- Combine or separate address parts
- Verify that each record has the same set of keys
"""


# -------------------------------------
# STEP 6: Export Users to CSV (Refactor with Helper)
# -------------------------------------
"""
Goal:
Adapt your CSV-writing logic (step 3) to a reusable helper function so both datasets
can be exported with the same pattern.

Tasks:
- Define export_to_csv(data, headers, filename) outside main()
- Wrap file-writing logic in try/except for error handling
- Comment out or remove the earlier Step 3 file-writing block
- Call export_to_csv() for both posts and users inside main()
- Confirm console messages show both CSVs written successfully
"""


# -------------------------------------
# MAIN PROGRAM STUB
# -------------------------------------
def main():
    """
    The main() function is the program’s entry point.
    You’ll add your fetch, normalize, and export logic here in later steps.
    """
    print("🚀 JSON to CSV Export Tool initialized.")
    print("(Follow the project steps to implement functionality.)\n")

    # Placeholder: your code will go here in later steps.
    # Start with STEP 1 imports and a simple print check.
    print("✅ Starter scaffold loaded successfully.")


# -------------------------------------
# RUNTIME ENTRY POINT
# -------------------------------------
if __name__ == "__main__":
    main()
