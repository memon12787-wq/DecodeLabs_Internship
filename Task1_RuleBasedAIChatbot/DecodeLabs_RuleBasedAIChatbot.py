from datetime import datetime
counter=0
print("WELCOME TO THIS BASIC AI CHATBOT")

def get_response(user_input,counter):
   inp_outDic={
      "hello":"Hi!",
      "how are you":"I'm fine! Thanks.",
      "who are you":"I'm a basic chatbot",
      "what is your name":"I'm a basic chatbot",
      "good morning":"Good Morning!",
      "good afternoon":"Good Afternoon!",
      "good evening":"Good Evening!",
      "thankyou":"You're welcome!",
      "thanks":"Happy to help!",
      "help":"Available commands: hello, how are you, who are you, what is your name, good morning, good afternoon, good evening, thankyou, thanks, bye",
      "bye":"Goodbye!"
   }
   return inp_outDic.get(user_input,"I don't understand that command. Type 'help' for a list of available commands.")


while True:  
  initial_inp=input("Ask Anything\n")
  user_input=initial_inp.lower().strip()
  counter=counter+1
  if user_input=="bye":
    print("Good bye!")
    break
  elif user_input=="time":
    print(datetime.now())
  elif user_input=="counter":
        print("You have asked "+str(counter)+" questions")
  else:
      print(get_response(user_input, counter))
