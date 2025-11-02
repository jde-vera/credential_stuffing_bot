import os
from app import create_app, db
from app.models import User

db_path = 'instance/users.db'

if os.path.exists(db_path):
    os.remove(db_path)
    print("existing database deleted...")

app = create_app()

with app.app_context():
    db.create_all()

    if User.query.count() == 0:
        user1 = User(username='john')
        user1.set_password('john123')

        user2 = User(username='jane')
        user2.set_password('janedoe')

        user3 = User(username='johnathan')
        user3.set_password('doe123')

        db.session.add_all([user1,user2,user3])
        db.session.commit()
        print("seeded default users: user1, user2, user3")