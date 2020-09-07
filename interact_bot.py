import random
from question_handlers import *
class InteractBot:
  def __init__(self, mainBot):
    self.mainBot = mainBot
    self.questions=[
      {"index":1,"ques":"Whats your scoring in the recent test or exam that you have taken ?","intent":"teachers"},
      {"index":2,"ques":"What Your Favrioute subject in school ?","intent":"teachers"},
      {"index":3,"ques":"Do your teachers give extra help when needed?","intent":"teachers"},
      {"index":4,"ques":"Do you Read Books Newspaper storybook or novels  ?","intent":"others"},
      {"index":5,"ques":"Who are your best friends in school ?","intent":"friends"},
      {"index":6,"ques":"Do Your parents allow you to play or be with your friends ?","intent":"parents"},
      {"index":7,"ques":"Do You think that your  parents try to control everything you do ?","intent":"parents"},
      {"index":8,"ques":"Do Your  parents encourge you to make your own decisions ?","intent":"parents"},
      {"index":9,"ques":"Do you enjoy doing your homeworks ?","intent":"teachers"},
      {"index":10,"ques":"Do you fear exams or tests  ?","intent":"teachers"},
      {"index":11,"ques":"Do you read or learn everyday at home?","intent":"teachers"},
      {"index":12,"ques":"What do you do at holidays?","intent":"others"},
      {"index":13,"ques":"Which sport do you like?","intent":"others"},
      {"index":14,"ques":"Do you participate in extra curicullar activities like dancing singing ?","intent":"others"},
      {"index":15,"ques":"Do you feel that your talents are not recognized well enough in your class?","intent":"teachers"},
      {"index":16,"ques":"what do you do when somone corrects your mistakes?","intent":"others"}
      ]
    self.totalQuestions = len(self.questions)
    self.subQuestion={
      "10":"Why? dont you have any favrioute subject ?",
      "11":"Why dont You like the other subjects?",
      "20":"How have they helped you ?",
      "21":"Have you asked for any help?",
      "30":"How much time do you usually spend",
      "40":"Do you have any friends other than your school friends?",
      "120":"how often do you play it",
      "130":"Do you like the activity which you have choosen?",
    }
    
  def interact(self):
    '''while(self.totalQuestions<4):'''
    answer=self.mainBot.getQA(self.questions)
    del self.questions[self.mainBot.questionIndex]
    self.totalQuestions=len(self.questions)
    self.mainBot.intent=self.questions[self.mainBot.questionIndex]["intent"]
    '''importName = "Question"+str(self.mainBot.question["index"])'''
    importName = "Question"+str(1)
    questionHandler=globals()[importName](self.mainBot)
    questionHandler.handle(answer)