#  firstly u need the python

import speech_recognition as sr #  and  install SpeechRecognition by useing the command line in ur terminal 'pip install SpeechRecognition'

import openai # now install openai to accses the openai(i.e chatgpt) u can get the openai key from the official website 'openai/api'

import pyttsx3 # this will help u to recordmthe audio use 'pip install pyttsx3'

engine = pyttsx3.init()
engine.setProperty('rate', 150)     #  change the 150 to rate of speed talk up the value to speed it up and down the value to down it
voicechanger=engine.getProperty('voices')
engine.setProperty('voice',voicechanger[1].id) #  for changing voice to male use replace voicechanger[1] with voicechanger[0]
count=0
engine.say('Hai, How can i help you')
engine.runAndWait()
while count<2:  #   u can set it to true and it will run contuosly untile u break it 
    count+=1
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.adjust_for_ambient_noise(source)  #  clears some background noise
        audio = r.listen(source)    
    try:
        text=r.recognize_google(audio)
        print(text)
        if 'stop' in text.lower():      #  whenever user gives command thats prasent stop init it will break the while
            engine.say('End of the program.')
            break
        openai.api_key = #  use your api key to get results
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        temperature=0.1,    # u can set the temp u high to get low chance for ai to get the same responce
        max_tokens=100,     #  this will give u max of 100 word of responce
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
        bla=response.get('choices')
        speaktext=bla[0].get('text')
        #  engine.setProperty('voice',voicechanger[0].id)
        engine.say(speaktext)
        print(speaktext)
        engine.runAndWait()

    except sr.UnknownValueError:
        print("Google could not understand audio")  # if no adiuo is recorded this will print
    except sr.RequestError as e:
        print("Google error; {0}".format(e))        # if any error it will print
    
    

    
