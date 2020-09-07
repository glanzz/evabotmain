import os
import random
import requests, json
import speech_recognition as speech_reco
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class MainBot:
  def __init__(self):
    '''reply from bot response from user'''
    self.sentimentAnalyze = SentimentIntensityAnalyzer()
    self.recoginizer = speech_reco.Recognizer()
    self.name = 'Dear'
    self.id = 0
    self.family_score = 0
    self.friends_score = 0
    self.teachers_score = 0
    self.rasa_url="http://127.0.0.1:5005/webhooks/rest/webhook"
    self.student_url = "http://127.0.0.1:3001/students"

  def reply_message(self, question):
    if isinstance(question, list):
      for ques in question:
        print("Bot:",ques)
        os.system("say "+str(ques))
    else:
      print("Bot:",question)
      os.system("say "+str(question))


  def init_database(self):
    send_data = [
      {
        "name": self.name,
        "school_id": "1am17xxxxx"
      }
    ]
    os.environ['no_proxy'] = '127.0.0.1,localhost'
    resp = requests.post(self.student_url, json = send_data)
    if resp.status_code == 200:
      response = resp.json()
      self.id = response.get("id",0)
    
    else:
      print("Error: Cannot set Counselling Data")
    
    

  def communicate_user(self,question):
    self.reply_message(question)
    try:
      with speech_reco.Microphone() as source:
        audio = self.recoginizer.listen(source)
      answer=self.recoginizer.recognize_google(audio)
    except:
      answer=""
    print("You:",answer)
    return answer
  
  
  def communicate_rasa(self, question):
    send_data = json.dumps({"message": question, "sender": self.id})
    os.environ['no_proxy'] = '127.0.0.1,localhost'
    resp = requests.post(self.rasa_url, data = send_data)
    if resp.status_code == 200:
      response = resp.json()
      responses = []
      for response_data in response:
        if response_data.get("buttons"):
          responses.append("Pardon Me! I did not get that Could you please rephrase what you said?")
        responses.append(response_data["text"])
    return responses
 
    
  def end_conversation(self):
    os.environ['no_proxy'] = '127.0.0.1,localhost'
    if self.id == 0:
      self.communicate_user("Thank You for your time. Have a good day Bye!!")
      return
    params = {"id": self.id}
    resp = requests.get(self.student_url, params = params)
    if resp.status_code == 200:
      response = resp.json()
      self.family_score = response.get("family_score",0)
      self.friends_score = response.get("friends_score", 0)
      self.teachers_score = response.get("teachers_score",0)
      self.name = response.get("name","Dear")
      self.summarize()
    else:
      print("Could not get scores")
    self.reply_message(f"Thank You for your time {self.name} ")
    self.reply_message("Bye! Good Luck")
  
  
  
  def summarize(self):
    family = {"neg": ["Your Parents may not always have time to spend with you but they will always would love to be with you an care about you.",
                   "They control you for good reasons so that you do not choose the wrong path in life"],
              "pos": ["Parents always have their love for you and would always support your decisions but not always take it positively"],
            }
    friends = {"neg": ["Friends are a gift in life do not miss the moments to be with friends because you may not get that again.",
                    "Make freinds if you do not have one"],
               "pos": ["Its right to enjoy with friends but keep your limits and try to concentrate on studies when required"]}
    teachers = {"neg": ["School is a second home. Scores do not decide your destiny.",
                        "Teachers may not be available every time they will also have works to handle",
                        "Ask teachers when you require help they will surely do it"],
                "pos": ["Schooling is a golden period.", "Try to concentrate on other subjects too even if you do not like it"]}
    summaries = ["I have some key points of our conversation which i would like to mention before you leave"]
    if self.family_score >= 0.3:
      summaries.append(family["pos"])
    if self.friends_score >= 0.3:
      summaries.append(friends["pos"])
    if self.teachers_score >= 0.3:
      summaries.append(teachers["pos"])
    if self.family_score < 0.3:
      summaries.append(family["neg"])
    if self.friends_score < 0.3:
      summaries.append(friends["neg"])
    if self.teachers_score < 0.3:
      summaries.append(teachers["neg"])
    self.reply_message(summaries)
  
  
  
  
  def start(self):
    self.init_database()
    rasa_response = self.communicate_rasa("Hello")
    user_response = self.communicate_user("Hello there!")
    if user_response and rasa_response:
      while(True):
        rasa_response = self.communicate_rasa(user_response)
        if 'Bye' in rasa_response:
          self.reply_message("Ok. So we have reached the end of our conversation!")
          self.end_conversation()
          break
        user_response = self.communicate_user(rasa_response)
        if not user_response:
          user_response = self.communicate_user("Sorry! I did not listen that properly could you please rephrase!!!")
    
      
      
    
    