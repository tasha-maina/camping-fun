🏕️ Camping Fun API

A simple Flask REST API for managing Campers, Activities, and Signups.
This API allows you to view campers, view activities, and create signups that connect campers to activities.

✅ Features

Manage Campers

Manage Activities

Create Signups linking campers ↔ activities

Validations for age and time

JSON API responses

Database migrations included

📁 Project Structure
camping-fun/
│
├── server/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── models.py
│   └── seed.py
│
├── migrations/
│
├── README.md
├── requirements.txt

🚀 How to Run the Project
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Set up the database

Run migrations:

flask db upgrade

3️⃣ Seed the database

python seed.py

4️⃣ Start the server
python -m server.app


Server runs on:

http://127.0.0.1:5555

📌 API Endpoints
👤 Campers
✅ Get all campers

GET /campers

✅ Get one camper

GET /campers/<id>

Returns camper info + their signups + activity info.

🎯 Activities
✅ Get all activities

GET /activities

✅ Delete an activity

DELETE /activities/<id>

Deletes the activity + any related signups.

📝 Signups
✅ Create a signup

POST /signups

Example body (JSON):

{
  "time": 12,
  "camper_id": 1,
  "activity_id": 1
}


Validations:

time must be between 0–23

Camper and activity IDs must exist

✅ Example Successful Signup Response
{
  "id": 3,
  "time": 12,
  "camper": {
      "id": 1,
      "name": "Cathy",
      "age": 12
  },
  "activity": {
      "id": 1,
      "name": "Archery",
      "difficulty": 3
  }
}

⚠️ Validation Error Example
{
  "errors": ["Time must be between 0 and 23"]
}

✨ Technologies Used

Flask

SQLAlchemy

Flask-Migrate

Postgres

Alembic

REST API JSON

✍️ Author

NATASHA ANASTASIA
