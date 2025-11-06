from server.config import db

class Signup(db.Model):
    # Name of the database table
    __tablename__ = "signups"

    # Primary key (unique identifier for each signup)
    id = db.Column(db.Integer, primary_key=True)

    # Time the camper chose for the activity (must always be provided)
    time = db.Column(db.Integer, nullable=False)

    # Foreign key linking the signup to a camper
    camper_id = db.Column(db.Integer, db.ForeignKey("campers.id"))

    # Foreign key linking the signup to an activity
    activity_id = db.Column(db.Integer, db.ForeignKey("activities.id"))

    def to_dict(self, include_nested=True):
        """
        Convert Signup object into a dictionary.
        
        include_nested:
            - True: include full camper + activity details
            - False: include only activity details
        """
        
        # Base data returned in all cases
        data = {
            "id": self.id,
            "camper_id": self.camper_id,
            "activity_id": self.activity_id,
            "time": self.time
        }

        # If nested data is requested
        if include_nested:
            data["camper"] = self.camper.to_dict()
            data["activity"] = self.activity.to_dict()
        else:
            # Only return activity if nested = False
            data["activity"] = self.activity.to_dict()

        return data
