class GreetBot():
  def __init__(self, mainBot):
    self.mainBot= mainBot
    self.introSenetences=["My name is Eva assistant counsellor", "For the next few minutes we shall have a conversation where most of the times I ask question and you would answer","I want you to be comfortable and Feel free to interact with me"]
    self.endGreetSentences=["So, Shall we start?","Can we Start?"]
    self.initGreetSentences=["Hello there, May I know your good name!","Hi buddy, What is your good name?", "Hello Buddy, What is your good name?"]
    self.retryText=["I did not get that could you repeat?", "Pardon me!"]

  def getName(self, text):
    defaultName="Dear" 
    names=[]
    processed_text=self.mainBot.nlp(text)
    for token in processed_text:
      if(token.lemma_ == token.text and token.pos_=="PROPN" and token.tag_=="NNP" and token.is_stop==False):
        names.append(token.text)
    if(self.mainBot.retry==2):
      self.mainBot.retry=0
      self.mainBot.askQuestion("Oh Dear! I did not get your name, Thats Fine Lets continue!")
      return [defaultName]
    if(len(names)==0):
      self.mainBot.retry+=1
      answer=self.mainBot.getAnswer(self.retryText[self.mainBot.retry-1]+" "+(self.mainBot.currentQuestion if self.mainBot.retry%2==0 else ''))
      names = self.getName(answer)
    return names

  def endGreet(self, text):
    sentimentScore = self.mainBot.sentimentAnalyze.polarity_scores(text)
    if sentimentScore['compound']>0:
      self.mainBot.askQuestion("Ok")
    else:
      self.mainBot.askQuestion("Never Mind ! I will continue even if its a No from you!!")
    self.mainBot.scores["others"]=sentimentScore["compound"]

  def greet(self):
    answer=self.mainBot.getQA(self.initGreetSentences)
    self.mainBot.studName=self.getName(answer)[0]
    self.mainBot.askQuestion("Nice to meet you "+self.mainBot.studName)
    for sentence in self.introSenetences:
      self.mainBot.askQuestion(sentence)
    answer=self.mainBot.getQA(self.endGreetSentences)
    self.endGreet(answer)
