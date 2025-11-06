from server.config import create_app, db
from server.models import Camper, Activity, Signup

app = create_app()

with app.app_context():
    print("Dropping existing tables...")
    db.drop_all()

    print("Creating new tables...")
    db.create_all()

    print("Seeding campers...")
    camper1 = Camper(name="Ashley", age=10)
    camper2 = Camper(name="Jordan", age=12)
    camper3 = Camper(name="Tasha", age=17)

    print("Seeding activities...")
    activity1 = Activity(name="Archery", difficulty=2)
    activity2 = Activity(name="Swimming", difficulty=3)
    activity3 = Activity(name="Arts & Crafts", difficulty=1)

    db.session.add_all([camper1, camper2, camper3, activity1, activity2, activity3])
    db.session.commit()

    print("✅ Seeding complete!")
