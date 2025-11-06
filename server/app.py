from flask import Flask, request, jsonify
from server.config import create_app, db
from server.models import Camper, Activity, Signup

# Create the Flask app using the factory pattern
app = create_app()


# -----------------------------
# CAMPERS ROUTES
# -----------------------------

@app.get("/campers")
def get_campers():
    """
    Return a list of all campers.
    """
    campers = Camper.query.all()
    return jsonify([c.to_dict() for c in campers]), 200


@app.get("/campers/<int:id>")
def get_camper(id):
    """
    Return a single camper by ID, including their signup info.
    """
    camper = Camper.query.get(id)
    if not camper:
        return {"error": "Camper not found"}, 404

    camper_data = camper.to_dict()

    # Include only signup details (activity + time)
    camper_data["signups"] = [
        s.to_dict(include_nested=False)
        for s in camper.signups
    ]

    return camper_data, 200


@app.post("/campers")
def create_camper():
    """
    Create a new camper.
    Validates that:
      - name is provided
      - age is an integer between 8 and 18
    """
    data = request.json
    name = data.get("name")
    age = data.get("age")

    # Validation rules
    if not name or not isinstance(age, int) or age < 8 or age > 18:
        return {"errors": ["validation errors"]}, 400

    camper = Camper(name=name, age=age)

    db.session.add(camper)
    db.session.commit()

    return camper.to_dict(), 201


@app.patch("/campers/<int:id>")
def update_camper(id):
    """
    Update an existing camper.
    Supports partial updates (name or age).
    """
    camper = Camper.query.get(id)
    if not camper:
        return {"error": "Camper not found"}, 404

    data = request.json

    # Update name if provided
    if "name" in data:
        camper.name = data["name"]

    # Update age if provided + validate it
    if "age" in data:
        if not isinstance(data["age"], int) or data["age"] < 8 or data["age"] > 18:
            return {"errors": ["validation errors"]}, 400
        camper.age = data["age"]

    db.session.commit()
    return camper.to_dict(), 202


# -----------------------------
# ACTIVITIES ROUTES
# -----------------------------

@app.get("/activities")
def get_activities():
    """
    Return a list of all activities.
    """
    activities = Activity.query.all()
    return jsonify([a.to_dict() for a in activities]), 200


@app.delete("/activities/<int:id>")
def delete_activity(id):
    """
    Delete an activity by ID.
    Returns 204 on successful deletion.
    """
    activity = Activity.query.get(id)
    if not activity:
        return {"error": "Activity not found"}, 404

    db.session.delete(activity)
    db.session.commit()

    return "", 204


# -----------------------------
# SIGNUPS ROUTES
# -----------------------------

@app.post("/signups")
def create_signup():
    """
    Create a new signup connecting:
       - a camper
       - an activity
       - a time slot (0–23)
    """
    data = request.json
    time = data.get("time")

    # Validate time (must be an integer hour)
    if not isinstance(time, int) or time < 0 or time > 23:
        return {"errors": ["validation errors"]}, 400

    signup = Signup(
        time=time,
        camper_id=data.get("camper_id"),
        activity_id=data.get("activity_id")
    )

    db.session.add(signup)
    db.session.commit()

    return signup.to_dict(), 201


# -----------------------------
# ENTRY POINT
# -----------------------------

if __name__ == "__main__":
    # Run on port 5555 as required by the assignment
    app.run(port=5555)
