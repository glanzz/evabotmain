from flask import Flask
from flask_restful import Api, Resource, reqparse,request
import logging
from Tables import UserInfo, PotentialReasons
from contextlib import contextmanager



app = Flask(__name__)
api = Api(app)
import logging
logging.basicConfig(filename='backend_error.log')

#####################################   
        
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
import sqlalchemy.orm



engine = create_engine("mysql+mysqldb://root:@localhost/evarasa",pool_size=20, pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session() 


#####################################

class StudentsManager(Resource):            
    def get(self):
      students=list()
      get_all=request.args.get('all', default=False)
      user_id=request.args.get('id', default=0)
      if get_all:
        for student_ID,student_name, school_id in session.query(UserInfo.id,UserInfo.name, UserInfo.school_id):
                students.append({"id":student_ID,
                                "name":student_name, 
                                "school_id": school_id, 
                                })
        return {"students":students}, 200
      if user_id:
        student_data = session.query(UserInfo.id,UserInfo.name,UserInfo.school_id,UserInfo.family_score, UserInfo.friends_score, UserInfo.teachers_score).filter(UserInfo.id==user_id)
        if student_data:
            print(student_data)
            student_id, student_name, school_id, family_score, friends_score, teachers_score = student_data.first()
            print(student_id)
            return {"id":student_id, 
                    "name": student_name, 
                    "school_id":school_id,
                    "family_score": family_score, 
                    "friends_score": friends_score, 
                    "teachers_score": teachers_score}, 200
      
      return {"Message": "No Student Found"}, 404

    def post(self):
      '''Send as array and get the data'''
      update_all=request.args.get('all', default=False)
      update_name = request.args.get('updateName', default=False)
      student_data = request.json
      if update_name:
        for student in student_data:
          user_id = student.get("id")
          name = student.get("user_name", "Dear")
          if user_id:
            session.query(UserInfo).filter(UserInfo.id==user_id).update(
                {
                  UserInfo.name: name
                }
              )
        return {"Message": "Update sucessfull"}, 200
      if student_data:
        for student in student_data:
          name = student.get("name")
          school_id = student.get("school_id")
          if name:
            user = UserInfo()
            user.school_id = school_id
            user.name = name
            session.add(user)
            session.commit()
          else:
            return {"Message": "No Name for an entry"}, 400
        if update_all:
          return {"Message":"Added Students"}, 200
        else:
          all_user_data = session.query(UserInfo.id,UserInfo.name,UserInfo.school_id, UserInfo.family_score, UserInfo.friends_score, UserInfo.teachers_score).filter(UserInfo.name==name)
          user_data = max(all_user_data, key=lambda item: item.id)
          return {"id": user_data.id, "name": user_data.name, "school_id": user_data.school_id, "family_score": user_data.family_score, "friends_score": user_data.friends_score, "teachers_score": user_data.teachers_score}, 200
      
        
      

class ScoresManager(Resource):            

    def post(self):
      '''Send as object and get the data'''
      student_data = request.json
      if student_data:
        try:
          family_score = float(student_data.get("family_score"))
          friends_score = float(student_data.get("friends_score"))
          teachers_score = float(student_data.get("teachers_score"))
          user_id = student_data.get("user_id")
          session.query(UserInfo).filter(UserInfo.id==user_id).update(
            {
              UserInfo.family_score: family_score,
              UserInfo.friends_score: friends_score,
              UserInfo.teachers_score: teachers_score
            }
          )
        except:
          return {"Message": "Invalid Data Given"}, 400
        return {"Message":"Added the Scores"}, 200
      else:
        return {"Message": "No Data Given"}, 400



class ReasonsManager(Resource):            
    def get(self):
      all_reasons=list()
      user_id=request.args.get('id', default=None)
      if user_id:
        user_exits = session.query(exists().where(UserInfo.id == user_id)).scalar()
        if user_exits:
          student_reasons = session.query(PotentialReasons.question,PotentialReasons.answer).filter(PotentialReasons.user_id==user_id).all()
          if student_reasons:
            for question, answer in student_reasons:
              all_reasons.append({"question":question, "answer": answer})
            return {"reasons":all_reasons}, 200
          else:
            return {"reasons": all_reasons}, 200
        return {"Message": "User Does Not exist"}
      return {"Message": "Requires ID"}, 404

    def post(self):
      reason = request.json
      if reason:
        question = reason.get("question")
        answer = reason.get("answer")
        user_id = reason.get("user_id")
        user_data = session.query(UserInfo.id).filter(UserInfo.id==user_id)
        try:
          user_data = user_data[0].id
        except:
          return {"Message":"Invaild ID"}, 400
        if question and answer and user_data:
          potential_reason = PotentialReasons()
          potential_reason.question = question
          potential_reason.answer = answer
          potential_reason.user_id = user_data
          session.add(potential_reason)
          session.commit()
        else:
          return {"Message": "No proper data for an entry"}, 400
        return {"Message":"Added to Reasons"}, 200
      else:
        return {"Message": "No Data Given"}



api.add_resource(ReasonsManager, "/reasons")
api.add_resource(StudentsManager, "/students")
api.add_resource(ScoresManager, "/scores")


app.run(port=3001, debug=True, threaded=True)

