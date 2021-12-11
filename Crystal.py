from nltk.stem.lancaster import LancasterStemmer
from googletrans import Translator
import speech_recognition as sr
from bs4 import BeautifulSoup
import face_recognition
from gtts import gTTS
import tensorflow
import datetime
import warnings
import calendar
import requests
import tflearn
import smtplib
import random
import pickle
import numpy
import json
import nltk
import cv2
import os

nltk.download('punkt')

icon = open('crystal_icon.txt', 'r')
print(icon.read())
icon.close()
muted = False

lang_dictionary = {
    'afrikaans': 'af',
    'albanian': 'sq',
    'amharic': 'am',
    'arabic': 'ar',
    'armenian': 'hy',
    'azerbaijani': 'az',
    'basque': 'eu',
    'belarusian': 'be',
    'bengali': 'bn',
    'bosnian': 'bs',
    'bulgarian': 'bg',
    'catalan': 'ca',
    'cebuano': 'ceb',
    'chichewa': 'ny',
    'chinese': 'zh-cn',
    'corsican': 'co',
    'croatian': 'hr',
    'czech': 'cs',
    'danish': 'da',
    'dutch': 'nl',
    'english': 'en',
    'esperanto': 'eo',
    'estonian': 'et',
    'filipino': 'tl',
    'finnish': 'fi',
    'french': 'fr',
    'frisian': 'fy',
    'galician': 'gl',
    'georgian': 'ka',
    'german': 'de',
    'greek': 'el',
    'gujarati': 'gu',
    'haitian creole': 'ht',
    'hausa': 'ha',
    'hawaiian': 'haw',
    'hebrew': 'he',
    'hindi': 'hi',
    'hmong': 'hmn',
    'hungarian': 'hu',
    'icelandic': 'is',
    'igbo': 'ig',
    'indonesian': 'id',
    'irish': 'ga',
    'italian': 'it',
    'japanese': 'ja',
    'javanese': 'jw',
    'kannada': 'kn',
    'kazakh': 'kk',
    'khmer': 'km',
    'korean': 'ko',
    'kurdish': 'ku',
    'kyrgyz': 'ky',
    'lao': 'lo',
    'latin': 'la',
    'latvian': 'lv',
    'lithuanian': 'lt',
    'luxembourgish': 'lb',
    'macedonian': 'mk',
    'malagasy': 'mg',
    'malay': 'ms',
    'malayalam': 'ml',
    'maltese': 'mt',
    'maori': 'mi',
    'marathi': 'mr',
    'mongolian': 'mn',
    'myanmar': 'my',
    'nepali': 'ne',
    'norwegian': 'no',
    'odia': 'or',
    'pashto': 'ps',
    'persian': 'fa',
    'polish': 'pl',
    'portuguese': 'pt',
    'punjabi': 'pa',
    'romanian': 'ro',
    'russian': 'ru',
    'samoan': 'sm',
    'scots gaelic': 'gd',
    'serbian': 'sr',
    'sesotho': 'st',
    'shona': 'sn',
    'sindhi': 'sd',
    'sinhala': 'si',
    'slovak': 'sk',
    'slovenian': 'sl',
    'somali': 'so',
    'spanish': 'es',
    'sundanese': 'su',
    'swahili': 'sw',
    'swedish': 'sv',
    'tajik': 'tg',
    'tamil': 'ta',
    'telugu': 'te',
    'thai': 'th',
    'turkish': 'tr',
    'turkmen': 'tk',
    'ukrainian': 'uk',
    'urdu': 'ur',
    'uyghur': 'ug',
    'uzbek': 'uz',
    'vietnamese': 'vi',
    'welsh': 'cy',
    'xhosa': 'xh',
    'yiddish': 'yi',
    'yoruba': 'yo',
    'zulu': 'zu'
}

# root = Tk()
file_r = open('lang.txt', 'r')
selected_lang_var = file_r.read()
# root.geometry("{0}x{1}+1+1".format(root.winfo_screenwidth(), root.winfo_screenheight()))
# root.minsize("200", "200")
# root.configure(bg="#1e243d")
# root.title("Crystal AI")
#
# muted = False
#
#
# def lang_back_func():
#     directions.pack_forget()
#     enter_text.pack_forget()
#     submit_button.pack_forget()
#     back_button.pack_forget()
#     selected_lang.pack_forget()
#     label_2.pack_forget()
#     crystal_speech.pack_forget()
#     time_l.pack_forget()
#     settings.pack_forget()
#     language.pack(pady=15, side=TOP)
#     gender.pack(pady=15, side=TOP)
#     color.pack(pady=15, side=TOP)
#     assis_name.pack(pady=15, side=TOP)
#     appearance.pack(pady=15, side=TOP)
#     people.pack(pady=15, side=TOP)
#     phrase.pack(pady=15, side=TOP)
#     back.pack(pady=20, side=TOP)
#
#
# def lang_func():
#     global directions
#     global enter_text
#     global submit_button
#     global back_button
#     language.pack_forget()
#     gender.pack_forget()
#     color.pack_forget()
#     assis_name.pack_forget()
#     appearance.pack_forget()
#     people.pack_forget()
#     phrase.pack_forget()
#     back.pack_forget()
#     directions = Label(text="Enter the language code for the language that you speak", bg='#1e243d',
#                        fg="white", font="comicsansms 20 bold", pady=15)
#     directions.pack(side=TOP, anchor="w", padx=25)
#     enter_text = Entry(root, width=50, bg="grey", font="comicsansms 20 bold")
#     enter_text.pack(side=TOP, anchor="w", padx=25)
#     back_button = Button(text="Back", fg="black", font="comicsansms 15 bold", pady=20, command=lang_back_func)
#     back_button.pack(side=BOTTOM, anchor="w", padx=25)
#
#     def submit():
#         global selected_lang_var
#         global selected_lang
#         selected_lang = Label(text="Your language: " + enter_text.get(), bg='#1e243d', fg="white",
#                               font="comicsansms 20 bold", pady=20)
#         selected_lang.pack(side=TOP, anchor="w", padx=25)
#         if enter_text.get() != "":
#             file_w = open('lang.txt', 'w')
#             file_w.write(enter_text.get())
#             selected_lang_var = file_r.read()
#         for i in lang_dictionary:
#             if selected_lang_var.lower() == i:
#                 selected_lang_var = lang_dictionary[i]
#
#     submit_button = Button(text="SUBMIT", bg='#1e243d', fg="black", font="comicsansms 20 bold", command=submit)
#     submit_button.pack(pady=15, padx=25, side=TOP, anchor="w")
#
#
# def mute():
#     global muted
#     muted = True
#
#
# def unmute():
#     global muted
#     muted = False
#
#
# def set_func():
#     global muted
#     global language
#     global gender
#     global color
#     global assis_name
#     global appearance
#     global people
#     global phrase
#     global back
#     global crystal
#     label_2.pack_forget()
#     crystal_speech.pack_forget()
#     time_l.pack_forget()
#     settings.pack_forget()
#     language = Button(text="LANGUAGE", bg='#1e243d', fg="black", font="comicsansms 25 bold", pady=18, padx=500,
#                       command=lang_func)
#     language.pack(pady=15, side=TOP)
#     gender = Button(text="GENDER", bg='#1e243d', fg="black", font="comicsansms 25 bold", pady=18, padx=515)
#     gender.pack(pady=15, side=TOP)
#     color = Button(text="COLOR", bg='#1e243d', fg="black", font="comicsansms 25 bold", pady=18, padx=520)
#     color.pack(pady=15, side=TOP)
#     assis_name = Button(text="NAME", bg='#1e243d', fg="black", font="comicsansms 25 bold", pady=18, padx=525)
#     assis_name.pack(pady=15, side=TOP)
#     appearance = Button(text="APPEARANCE", bg='#1e243d', fg="black", font="comicsansms 25 bold", pady=18, padx=480)
#     appearance.pack(pady=15, side=TOP)
#     people = Button(text="PEOPLE", bg='#1e243d', fg="black", font="comicsansms 25 bold", pady=18, padx=515)
#     people.pack(pady=15, side=TOP)
#     phrase = Button(text="WISH PHRASE", bg='#1e243d', fg="black", font="comicsansms 25 bold", pady=18, padx=477)
#     phrase.pack(pady=15, side=TOP)
#     back = Button(text="BACK", bg='red', fg="black", font="comicsansms 15 bold", pady=18, command=home_func)
#     back.pack(pady=20, side=TOP)
#     muted = True
#
#
# def home_func():
#     global muted
#     language.pack_forget()
#     gender.pack_forget()
#     color.pack_forget()
#     assis_name.pack_forget()
#     appearance.pack_forget()
#     people.pack_forget()
#     phrase.pack_forget()
#     back.pack_forget()
#     label_2.pack(fill=X, pady=10, side=BOTTOM)
#     crystal_speech.pack(pady=15, side=BOTTOM)
#     time_l.pack(anchor="w", side=TOP)
#     settings.pack(anchor="se", pady=1, padx=1)
#     muted = False
#
#
# label_2 = Label(text="You said:", bg='#1e243d', fg="green", font="comicsansms 20 bold")
# label_2.pack(fill=X, pady=10, side=BOTTOM)
# crystal_speech = Label(text="Hello!", bg='#1e243d', fg="white", font="comicsansms 25 bold")
# crystal_speech.pack(pady=15, side=BOTTOM)
# time_l = Label(text="", bg='#1e243d', fg="yellow", font="comicsansms 25 bold")
# time_l.pack(anchor="w", side=TOP)
# settings = Button(text='settings', anchor="se", command=set_func)
# settings.pack(anchor="se", pady=1, padx=1)

stemmer = LancasterStemmer()

warnings.filterwarnings('ignore')
first = "Vatsal"
last = "Dutt"


def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 465)
    server.ehlo()
    server.starttls()
    server.login('vatdut8994@gmail.com', '')
    server.sendmail('vatdut8994@nrms.org', to, content)
    server.close()

def assis_trans(sen):
    translator = Translator()
    try:
        translate_text = translator.translate(sen, src='en', dest=selected_lang_var).text
        print(translate_text)
    except AttributeError:
        translate_text = translator.translate(sen, src='en', dest=selected_lang_var).text
        speak_female(translate_text[0])
        speak_female(translate_text[1])
    return translate_text


def speak_female(audio):
    # crystal_speech['text'] = audio
    if selected_lang_var == 'en':
        print(str(audio))
    else:
        print(str(audio))
        audio = assis_trans(audio)
        print(str(audio))
    my_obj = gTTS(text=audio, lang=selected_lang_var, slow=False)
    my_obj.save('audio.mp3')
    os.system('mpg123 audio.mp3')
    os.remove('audio.mp3')


def translate(sen):
    translator = Translator()
    try:
        translate_text = translator.translate(sen, src=selected_lang_var, dest='en').text
    except AttributeError:
        translate_text = translator.translate(sen, src=selected_lang_var, dest='en').text
        speak_female(translate_text[0])
        speak_female(translate_text[1])
    return translate_text


def intro():
    speak_female("I am Crystal how may I help you?")


def wish_me(person):
    hr = int(datetime.datetime.now().hour)
    if 0 < hr < 12:
        speak("Good Morning " + person.lower().title() + "!")

    elif 12 <= hr <= 16:
        speak("Good Afternoon " + person.lower().title() + "!")

    else:
        speak("Good Evening " + person.lower().title() + "!")
    intro()


def wake_word(word):
    wake_words = ['crystal', 'dude']

    word = word.lower()

    for phr in wake_words:
        if phr in word:
            return True

    return False


def web_scrapper(input_data_to_search):
    source = requests.get('https://www.google.com/search?q=' + input_data_to_search).text
    soup = BeautifulSoup(source, 'lxml')

    ans = None
    list1 = []
    list2 = []

    for i in soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd'):
        for j in i.find_all('div', class_='BNeawe s3v9rd AP7Wnd'):
            list2.append(j.text)
            list1.append(str(j.text).split(' '))
            try:
                ans = soup.find('div', class_='BNeawe iBp4i AP7Wnd').text
            except AttributeError:
                if list1[-1][-1] == 'Wikipedia':
                    ans = j.text

                else:
                    try:
                        if "\n" in list2[1]:
                            ans = list2[0].split('\n')[1]
                        else:
                            if list2[0] == 'noun\n':
                                ans = list2[1]
                            elif list2[0] == 'adjective\n':
                                ans = list2[1]
                            elif list2[0] == 'verb\n':
                                ans = list2[1]
                            elif list2[0] == 'adverb\n':
                                ans = list2[1]
                            elif list2[0] == 'preposition\n':
                                ans = list2[1]
                            else:
                                ans = list2[0]
                    except:
                        pass

    if ans is None:
        ans = list2[0]

    return ans


speak = speak_female

sorry_list = ["I am sorry, I could not understand that",
              "I am not sure I understand that",
              "I am sorry, I don't get that"]

with open("intents.json") as file:
    data = json.load(file)

try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words = []
    labels = []
    docs_x = []
    docs_y = []

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)

    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w.lower()) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = numpy.array(training)
    output = numpy.array(output)

    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

tensorflow.compat.v1.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

try:
    model.load("model.tflearn")
except:
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("model.tflearn")


def bag_of_words(s, wrd):
    bag2 = [0 for _ in range(len(wrd))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(wrd):
            if w == se:
                bag2[i] = 1

    return numpy.array(bag2)


path = 'img/known/'
images = []
classNames = []
myList = os.listdir(path)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

cap = cv2.VideoCapture(0)
name = ''

with open('face_rec', 'rb') as file:
    encodeListKnown = pickle.load(file)

while name == '':
    success, img = cap.read()
    img = cv2.flip(img, 2)
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print(faceDis)
        matchIndex = numpy.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (205, 154, 79))
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (205, 154, 79), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)
cap.release()
wish_me(name)


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        print("Recognizing...")
    dt = ''
    try:
        dt = r.recognize_google(audio, language=selected_lang_var)
        # label_2['text'] = "You said: " + dt
        print("You said: " + dt)

    except sr.UnknownValueError:
        print("Sorry, I could not understand that try saying it again")

    except sr.RequestError:
        print("Request results from Google Speech Recognition service error")

    english = translate(dt)
    print(english)
    return english


def chat():
    if muted is False:
        inp = command()
        inp = inp.lower()
        if wake_word(inp) is True:
            inp = inp.replace('crystal', '')
            response = ''
            results = model.predict([bag_of_words(inp, words)])[0]
            results_index = numpy.argmax(results)
            tag = labels[int(results_index)]

            if results[results_index] > 0.7:
                for tg in data["intents"]:
                    if tg['tag'] == tag:
                        responses = tg['responses']
                        response = random.choice(responses)

            elif inp == "":
                print("")

            else:
                response = response + web_scrapper(inp)

            if inp.lower().replace('crystal', '') == 'quit':
                speak_female(response)
                quit()

            if tag == 'read document':
                exec(open('scanner.py').read())

            if tag == "emailMom":
                try:
                    speak_female("What should I say to mom")
                    content = inp
                    to = "gdatt22@gmail.com"
                    send_email(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    speak_female(e)
                    response = response + "Sorry Sir the could not be sent"

#             try:
#                 crystal_speech['text'] = response
            speak(response)
#
#             except AssertionError:
#                 crystal_speech['text'] = ""
#
#                 crystal_speech['text'] = ""
#
#             if crystal_speech['text'] == "":
#                 print('', end='')
#
#             elif len(crystal_speech['text']) >= 500:
#                 crystal_speech['text'] = crystal_speech['text'][0:100] + '\n' + crystal_speech['text'][100:200] \
#                                          + '\n' + crystal_speech['text'][200:300] + '\n' + crystal_speech['text'][
#                                                                                            300:400] \
#                                          + '\n' + crystal_speech['text'][400:500] + '\n' + crystal_speech['text'][
#                                                                                            500:601]
#
#             elif 500 >= len(crystal_speech['text']) >= 400:
#                 crystal_speech['text'] = crystal_speech['text'][0:100] + '\n' + crystal_speech['text'][100:200] \
#                                          + '\n' + crystal_speech['text'][200:300] + '\n' + crystal_speech['text'][
#                                                                                            300:400] \
#                                          + '\n' + crystal_speech['text'][400:501]
#
#             elif 400 >= len(crystal_speech['text']) >= 300:
#                 crystal_speech['text'] = crystal_speech['text'][0:100] + '\n' + crystal_speech['text'][100:200] \
#                                          + '\n' + crystal_speech['text'][200:300] + '\n' + crystal_speech['text'][
#                                                                                            300:401]
#
#             elif 300 >= len(crystal_speech['text']) >= 200:
#                 crystal_speech['text'] = crystal_speech['text'][0:100] + '\n' + crystal_speech['text'][100:200] \
#                                          + '\n' + crystal_speech['text'][200:301]
#
#             elif 100 >= len(crystal_speech['text']) >= 100:
#                 crystal_speech['text'] = crystal_speech['text'][0:100] + '\n' + crystal_speech['text'][100:200]
#     root.after(1000, chat)
#
#
# root.after(1000, chat)
# root.mainloop()
