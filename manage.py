
from flask import Flask,request,jsonify
app = Flask(__name__)

from models.Users import User,db

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/users',methods=['GET','POST','PUT','DELETE'])
@app.route('/users/<int:id>',methods=['GET','POST','PUT','DELETE'])
def user(id=None):
    
    if request.method == 'GET':
        try:
            if id:
                user = User.query.filter_by(id=id).first()
                users = user.toDict()
            else:
                users = User.query.all()
                if users:
                    res=[]
                    for row in users:
                        
                        res.append(row.toDict())
                    users = res
            
            return jsonify({'message':'Users Data','data':users})
        except Exception as err:
            return jsonify({'status':False,'message':'Unable to Get Users Data', 'devMsg':str(err)})

    if request.method == 'POST':
        try:
            payload = request.get_json()
            id = payload.get('id')
            name = payload.get('name')
            age = payload.get('age')
            attendance = payload.get('attendance')
            user = User(id,name,age,attendance)
            db.session.add(user)
            db.session.commit()
            return jsonify({'status':True,'message':'User Added Successfully'})
        except Exception as err:
            return jsonify({'status':False,'message':'Unable to Add User', 'devMsg':str(err)})



app.run()#(port=8080,debug=True)
