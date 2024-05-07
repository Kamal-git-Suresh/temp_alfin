from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
#from crypto.Cipher import AES
#import base64

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///donor.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.db'
db = SQLAlchemy(app)

#def encrypt_data(data):
#    key = b'hhhkjkl;'
#    iv = b'ljkgyjnk'
#    cipher = AES.new(key, AES.MODE_CBC, iv)
#    encrypted_data = cipher.encrypt(data.encode())
#    return base64.b64encode(encrypted_data).decode()
#
#def decrypt_data(data):
#    key = b'hhhkjkl'
#    iv = b'ljkgyjnk'
#    decoded_data = base64.b64decode(data.encode())
#    cipher = AES.new(key, AES.MODE_CBC, iv)
#    decrypted_data = cipher.decrypt(decoded_data).decode()
#    #return decrypted_data

class Donor(db.Model):
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
    
class Recipient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    blood_group = db.Column(db.String(10), nullable=False)
    location_x = db.Column(db.String(100), nullable=False)
    location_y = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return f'<Recipient {self.name}>'
    
class Doctor(db.Model):
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
    id = db.Column(db.String(20), primary_key=True, unique = True)
    password = db.Column(db.String(20), primary_key=False)
    def __repr__(self):
        return f'<Login {self.id}>'
    
@app.route('/insert_donor', methods=['get'])
def insert_donor():
    #data = request.get_json()
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

@app.route('/insert_recipient', methods=['get'])
def insert_recipient():
    #data = request.get_json()
    print('donor works')
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')
    blood_group = request.args.get('blood_group')
    location_x = request.args.get('location_x')
    location_y = request.args.get('location_y')

    new_donor = Recipient(name=name, email=email, phone=phone, blood_group=blood_group, location_x=location_x,location_y=location_y)
    db.session.add(new_donor)
    db.session.commit()

    return jsonify({'message': 'Donor added successfully'})

@app.route('/insert_doctor', methods=['get'])
def insert_doctor():
    #data = request.get_json()
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

    return jsonify({'message': 'Doctor added successfully'})

@app.route('/insert_login', methods=['get'])
def insert_login():
    #data = request.get_json()
    print('this function works')
    id = request.args.get('id')
    password = request.args.get('password')
    print(id, password)
    new_login = Login(id = id, password = password)
    db.session.add(new_login)
    db.session.commit()

    return jsonify({'message': 'Login added successfully'})

@app.route('/get_donor', methods=['get'])
def get_donor():
    print(Donor.query.all())
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