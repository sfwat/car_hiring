from flask import app, jsonify, g


class Customer:
    def __init__(self, name=None, email=None, phone=None, id=None):
        self.username = name
        self.email = email
        self.phone = phone
        self.id = id

    def create(self):
        query = """insert into `customers` (username, email, phone) values (%s, %s, %s) """
        db = g.db
        cur = db.cursor()
        cur.execute(query, (self.username, self.email, self.phone))
        db.commit()
        cur.close()
        return jsonify({"message": "successfully inserted"}), 201

    def get(self):
        query = """select * from `customers` where  customerId = %s"""
        db = g.db
        cur = db.cursor()
        cur.execute(query, self.id)
        customer = cur.fetchone()
        cur.close()
        if not customer:
            return jsonify({"message": f"customer with Id {self.id} does not exist"}), 404
        return jsonify({"customer": customer}), 200

    def delete(self):
        query = """delete  from `customers` where  customerId = %s"""
        db = g.db
        cur = db.cursor()
        deleted = cur.execute(query, self.id)
        if not deleted:
            cur.close()
            return jsonify({"message": f"customer with Id {self.id} does not exist"}), 404
        db.commit()
        cur.close()
        return jsonify({"message": "successfully deleted"}), 200
