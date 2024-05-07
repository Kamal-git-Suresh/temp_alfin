from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from cryptography.fernet import Fernet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///donor.db'
db = SQLAlchemy(app)

# AES encryption key
encryption_key = Fernet.generate_key()
fernet = Fernet(encryption_key)

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    blood_group = db.Column(db.String(10), nullable=False)
    location_x = db.Column(db.String(100), nullable=False)
    location_y = db.Column(db.String(100), nullable=False)

class Donor(BaseModel):
    __tablename__ = 'donors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    blood_group = db.Column(db.String(10), nullable=False)
    location_x = db.Column(db.String(100), nullable=False)
    location_y = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return f'<Donor {self.name}>'
    def __str__(self) -> str:
        return self.id, self.name, self.email, self.blood_group

class Recipient(BaseModel):
    __tablename__ = 'recipients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    blood_group = db.Column(db.String(10), nullable=False)
    location_x = db.Column(db.String(100), nullable=False)
    location_y = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return f'<Recipient {self.name}>'

class Doctor(BaseModel):
    __tablename__ = 'doctors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    blood_group = db.Column(db.String(10), nullable=False)
    location_x = db.Column(db.String(100), nullable=False)
    location_y = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return f'<Recipient {self.name}>'

class Login(db.Model):
    id = db.Column(db.String(20), primary_key=True, unique=True)
    password = db.Column(db.String(20), primary_key=False)

@app.route('/insert_donor', methods=['POST'])
def insert_donor():
    print('donor works')
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')
    blood_group = request.args.get('blood_group')
    location_x = request.args.get('location_x')
    location_y = request.args.get('location_y')

    new_donor = Donor(name=name, email=email, phone=phone, blood_group=blood_group, location_x=location_x,location_y=location_y)
    db.session.add(new_donor)
    db.session.commit()

    return jsonify({'message': 'Donor added successfully'})
@app.route('/insert_recipient', methods=['POST'])
def insert_recipient():
    #  print('donor works') 
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')
    blood_group = request.args.get('blood_group')
    location_x = request.args.get('location_x')
    location_y = request.args.get('location_y')

    new_donor = Recipient(name=name, email=email, phone=phone, blood_group=blood_group, location_x=location_x,location_y=location_y)
    db.session.add(new_donor)
    db.session.commit()

@app.route('/insert_doctor', methods=['POST'])
def insert_doctor():
    print('doctor works')
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')
    blood_group = request.args.get('blood_group')
    location_x = request.args.get('location_x')
    location_y = request.args.get('location_y')

    new_doctor = Doctor(name=name, email=email, phone=phone, blood_group=blood_group, location_x=location_x,location_y=location_y)
    db.session.add(new_doctor)
    db.session.commit()

    return jsonify({'message': 'Doctor added successfully'})# similar implementation to insert_donor

@app.route('/insert_login', methods=['POST'])
def insert_login():
    data = request.get_json()
    try:
        login = Login(id=data['id'], password=fernet.encrypt(data['password'].encode()))
        db.session.add(login)
        db.session.commit()
        return jsonify({'message': 'Login added successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/get_donor', methods=['get'])
def get_donor():
    print(type(Donor.query.all()))
    return jsonify({'contents':Donor.query.all()})
'''
@app.route('/insert_donor', methods=['POST'])
def insert_donor():
    data = request.get_json()
    name = data['name']
    email = data['email']
    phone = data['phone']
    blood_group = data['blood_group']
    #location = data['location']

    new_donor = Donor(name=name, email=email, phone=phone, blood_group=blood_group, location=location)
    db.session.add(new_donor)
    db.session.commit()

    return jsonify({'message': 'Donor added successfully'})
'''
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)