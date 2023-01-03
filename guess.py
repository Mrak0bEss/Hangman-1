from Levenshtein import distance
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

import random

from printhang import PrintHang
from equal import Sravnenie

#класс хранит методы работы с алгоритмическим отгадыванием слова
class HangmanGuessingRus:
    #создание сета ближайших слов
    def sett(lines,hide):
        setword=set()
        max=0
        min=0
        
        for wrds in lines:
            if len(wrds)==len(hide) and Sravnenie.chek(hide,wrds):
                if fuzz.ratio(hide,wrds)>max:
                    setword=set()
                    setword.add(wrds)
                    min=distance(wrds,hide)
                    max =fuzz.ratio(hide,wrds)
                if fuzz.ratio(hide,wrds)==max:
                    setword.add(wrds)
        return setword
    #функция берет слово из сета, находит букву, которая еще не открыта и может быть в слове, и предлагает ее игроку
    def Guess(hide,setword,sets) -> tuple:
            
        ind= 0
        if len(setword)==1:
            return hide, ' ', ind,setword
            
        else:
         
            while(1):
                x = setword.pop()
                for i in range(len(x)):
                    
                    if (x[i] not in sets[i]):
                        ind = i
                        
                        if (hide[ind]=='_'):
                            
                            return hide, x, ind,setword
                    
                
        return hide, x, ind,setword
    #функция создает базу всех слов и искомую маску слова готовит к обработке
    def Var(hide    )->tuple:
           
            hide1=[None]*len(hide)
            for i in range(len(hide)):
                #  print(i)
                hide1[i]=hide[i]
            #print(hide)     
            with open('singular_and_plural.txt', encoding='utf-8') as f:
                lines = f.read().splitlines()
            return hide1,lines
     

