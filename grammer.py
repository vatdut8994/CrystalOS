# phrase = 'Hello World, I am Vatsal Dutt. I like coding and chess, but they are addicting. Coding hurts your eyes, while chess hurts your brain.'

# phrase = phrase.split('.')
# finalPhrase = []
# for element in phrase:
#     for phrases in element.split(','):
#         finalPhrase.append(phrases)

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup

def parts_of_speech(text):
    PATH = "D:/chromedriver.exe"
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op, service=Service(PATH))

    driver.get('https://parts-of-speech.info/')
    text_cookie = driver.find_element(By.ID, 'text')

    text_cookie.click()
    text_cookie.clear()
    text_cookie.send_keys(text)

    submit_cookie = driver.find_element(By.ID, 'submit')
    submit_cookie.click()

    html_source_code = driver.execute_script("return document.body.innerHTML;")
    soup = BeautifulSoup(html_source_code, 'html.parser')

    soup.find_all('span', class_='taggedWord')

    span = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "taggedWord"))
    )
    div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "textTagged"))
    )
    words = div.find_elements(By.TAG_NAME, "span")
    pos = []
    posWords = []
    for word in words:
        for className in word.get_attribute('class').split():
            if 'tag' in className and 'tagged' not in className:
                pos.append(className.replace('tag', '').lower())
        posWords.append(word.text)
    driver.quit()

    other = []
    noun = []
    adjective = []
    adverb = []
    conjunction = []
    determiner = []
    number = []
    preposition = []
    pronoun = []
    verb = []
    for num in range(len(posWords)):
        if pos[num] == 'other':
            other.append(posWords[num])
        elif pos[num] == 'noun':
            noun.append(posWords[num])
        elif pos[num] == 'adjective':
            adjective.append(posWords[num])
        elif pos[num] == 'adverb':
            adverb.append(posWords[num])
        elif pos[num] == 'conjunction':
            conjunction.append(posWords[num])
        elif pos[num] == 'determiner':
            determiner.append(posWords[num])
        elif pos[num] == 'number':
            preposition.append(posWords[num])
        elif pos[num] == 'pronoun':
            pronoun.append(posWords[num])
        elif pos[num] == 'verb':
            verb.append(posWords[num])
        elif pos[num] == 'pronoun':
            pronoun.append(posWords[num])

    subject = []
    predicate = []
    for n in noun:
        subject.append(n)

    for pn in pronoun:
        subject.append(pn)

    for v in verb:
        predicate.append(v)

    # print(other)
    # print(noun)
    # print(adjective)
    # print(adverb)
    # print(conjunction)
    # print(determiner)
    # print(number)
    # print(preposition)
    # print(pronoun)
    # print(verb)
    return {'other':other, 'noun':noun, 'adjective':adjective, 'adverb':adverb, 'conjunction':conjunction, 'determiner':determiner,
     'number':number, 'preposition':preposition, 'pronoun':pronoun, 'verb':verb, 'subject':subject, 'predicate':predicate}

other, noun, adjective, adverb, conjunction, determiner, number, preposition, pronoun, verb, subject, predicate = parts_of_speech("Show the whole house").values()

print(subject)
print(other, noun, adjective, adverb, conjunction, determiner, number, preposition, pronoun, verb, subject, predicate)