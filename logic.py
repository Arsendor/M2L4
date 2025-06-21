# Задание №3
from translate import Translator
import requests
from collections import defaultdict

# Задание №5
questions = {'как тебя зовут' : "Я супер-крутой-бот и мое предназначение помогать тебе!",
             "сколько тебе лет" : "Это слишком философский вопрос"}

class TextAnalysis():   
    
    # Задание №1
    memory = defaultdict(list)
    
    def __init__(self, text, owner):

        # Задание №2
        TextAnalysis.memory[owner].append(self)
        self.text = text
        self.translation = self.__translate(self.text, "ru", "en")

        # Задание №6
        if self.text.lower() in questions.keys():
            self.response = questions[self.text.lower()]
        else: 
            self.response = self.get_answer()

    
    def get_answer(self):
        res = self.__translate("I don't know how to help", "en", "ru")
        return res

    def __translate(self, text, from_lang, to_lang):
        try:
            # Задание №4
            translator = Translator(from_lang='ru', to_lang='en')
            translation = translator.translate(text)
            return translation
        except:
            return "Перевод не удался"