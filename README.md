# fire-safety-equipment-tracker
🔥 Fire Safety Equipment Inspection & Expiry Register
📌 Problem Statement

Fire safety equipment in buildings is usually tracked using paper tags, leading to missed inspections and expired units.
This project provides a digital tracking system to monitor inspection dates, calculate expiry, and alert overdue equipment.

🎯 Objective

To build a system that:

Stores safety equipment details
Automatically calculates next inspection date
Identifies overdue and due equipment
Helps safety officers monitor and act quickly
🛠️ Technologies Used
Frontend: HTML, CSS, JavaScript
Data Storage: JSON file (data.json)
Machine Learning: Python (scikit-learn)
📁 Project Structure
📦 Fire-Safety-Tracker
 ┣ 📄 index.html
 ┣ 📄 style.css
 ┣ 📄 script.js
 ┣ 📄 data.json
 ┣ 📄 model.py
 ┗ 📄 README.md
📊 Dataset Description

The dataset contains 100 records with the following fields:

Field Name	Description
record_id	Unique record number
equipment_id	Equipment identifier (e.g., FE-101)
type	Type of extinguisher (CO2, Foam, Water)
building	Building name
floor	Floor number
last_inspection	Last inspection date
next_due	Next due date (optional, auto-calculated)
status	OK / DUE / OVERDUE
remarks	Notes about equipment
outcome	Target variable for ML (0 = Safe, 1 = Risk)
⚠️ Edge Cases Included
Missing values (empty fields)
Similar names (Block A vs Block-A)
Invalid record (floor = 0, Block X)
⚙️ Key Features
🔍 1. Search & Filter
Live search by equipment ID
Filter by status (OK, DUE, OVERDUE)
Displays number of records dynamically
📋 2. Equipment Table
Displays key details:
ID
Type
Building
Next Due
Status
📌 3. Detail View
Opens when a record is clicked
Shows full equipment details
Displays derived value at the top:
Days remaining OR overdue days
🔄 4. Auto Calculation (Important Feature)

The system dynamically calculates:

next_due = last_inspection + 6 months

This ensures:

No dependency on static data
Always up-to-date results
🤖 5. Machine Learning Model
Built using Decision Tree Classifier
Predicts whether equipment is:
✅ Safe
⚠️ At Risk
Features Used:
Floor
Days since last inspection
Important:
Avoided data leakage (did not use status/next_due)
▶️ How to Run the Project
🔹 Step 1: Open Frontend
Open index.html in browser
🔹 Step 2: Run ML Model

Install dependencies:

pip install pandas scikit-learn

Run:

python model.py
🧪 Testing

✔ Search and filter tested
✔ Edge cases handled (missing values)
✔ Derived values verified manually
✔ No blank or error screens
🔐 Limitations
No authentication system (single-user system)
Data stored in JSON (not secure for production)
ML model is basic and uses limited features
🚀 Future Improvements
Add login authentication
Store data in database (MySQL / Firebase)
Improve ML model accuracy
Add alerts/notifications for overdue equipment
🎥 Demo
Screenshots included in repository
Demo video shows:
Search & filter
Detail view
Prediction
🎤 Conclusion

This project demonstrates a simple yet effective system to track fire safety equipment, automate inspection calculations, and assist in decision-making using machine learning.

👩‍💻 Author

Akshaya Shree G
B.Tech Artificial Intelligence & Data Science
PDKVCET
