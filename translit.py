# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def translit_to_eng(ru_text):
    ru_alphabet = u"абвгдеёжзийклмнопрстуфхцчшщьыъяюэ"
    en_translit = ['a','b','v','g','d','ye','yo','zh','z','i','y','k','l','m','n','o','p','r','s','t','u','f','h','ts','ch','sh','shch',"'",'y','"','ja','ju','e']
    translited_list = []
    # Достаём по одному символу(symbol) из входного предложения(ru_text)
    for symbol in ru_text:
    	# Проверка символа на верхность регистра :)
        low_flag = False
    	if symbol.islower() == False:
    		# Уменьшение регистра символа, и поднятие флажка наличия символа с изменённым регистром
    		symbol = symbol.lower()
    		low_flag = True

    	# Достаём по одной букве(ru_symbol) из русского алфавита(ru_alphabet)
        for i in range(len(ru_alphabet)):
        	# Проверяем на одинаковость входной символ и символ из алфавита
            if ru_alphabet[i] == symbol:
            	# Добавляем в масив символов(translited_list) символ(en_translit[i]), удовлетворяющий условию
            	if low_flag == False:
            		translited_list.append(en_translit[i])
            	elif low_flag == True:
            		translited_list.append(en_translit[i].capitalize())
            		low_flag == False
                break
            # Проверка, является ли символ небуквой(цыфра, пробел, пунктуационный знак...)
            elif symbol.isalpha() == False:
            	translited_list.append(symbol)
            	break

    translited_string = ''.join(translited_list)
    return translited_string

n = u"Привет!!!! Меня зовут Роман."
print translit_to_eng(n)

