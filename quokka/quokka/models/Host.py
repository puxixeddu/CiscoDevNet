from quokka import db


class Host(db.Model):

    __tablename__ = "host"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    ip_address = db.Column(db.Text, nullable=False)
    mac_address = db.Column(db.Text)

    availability = db.Column(db.Boolean)
    response_time = db.Column(db.Integer)

    last_heard = db.Column(db.Text)

    def __repr__(self):
        return f"Host: {self.name}"
