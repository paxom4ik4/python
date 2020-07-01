import sys
import random



# слова и ответы

# level_1
level1_1 = ("    1 2 3 4\n", "A   ц в а к", "B   с г ч ч", "C   ы т о у", "D   п ъ р р")
level1_2 = ("    1 2 3 4\n", "A   ц г т л", "B   с п л о", "C   ы т о щ", "D   к ь д а")
level1_3 = ("    1 2 3 4\n", "A   в т о к", "B   ч и р я", "C   о н ю ф", "D   м э л е")
level1_4 = ("    1 2 3 4\n", "A   в о л о", "B   п н к к", "C   р о а й", "D   е т ь ж")
level1_5 = ("    1 2 3 4\n", "A   х п о р", "B   м з д с", "C   о а у к", "D   л к ш ц")

ans_level1_1 = "D4 РУЧКА"
level1_1_coord = "D4"
ans_level1_2 = "B2 ПЛОЩАДЬ"
level1_2_coord = "B2"
ans_level1_3 = "D1 МОНИТОР"
level1_3_coord = "D1"
ans_level1_4 = "B4 КОЛОНКА"
level1_4_coord = "B4"
ans_level1_5 = "A2 ПОДУШКА"
level1_5_coord = "A2"


# level_2 
level2_1 = ("    1 2 3 4 5\n", "A   у ы в е а", "B   в с е ш ы", "C   в ц ф а л", "D   ц ы й а к", "E   ы к к я й")
level2_2 = ("    1 2 3 4 5\n", "A   к ц п к н", "B   к с т у ы", "C   е ф е ц ь", "D   ч й к л й", "E   я к й о я")
level2_3 = ("    1 2 3 4 5\n", "A   ц у й я а", "B   й ч й ч к", "C   к ч ц о м", "D   е ы у л н", "E   ц с б ц я")
level2_4 = ("    1 2 3 4 5\n", "A   ц ф г а с", "B   п х ш р у", "C   а в и а т", "D   л к н э з", "E   р е и м п")
level2_5 = ("    1 2 3 4 5\n", "A   з б е т в", "B   а р т р ы", "C   д ь д ю у", "D   е л с к г", "E   ф и ч н б")

ans_level2_1 = "A3 ВЕШАЛКА"
level2_1_coord = "A3"
ans_level2_2 = "B2 СТЕКЛО"
level2_2_coord = "B2"
ans_level2_3 = "E3 БУЛОЧКА"
level2_3_coord = "E3"
ans_level2_4 = "D2 КЛАВИАТУРА"
level2_4_coord = "D2"
ans_level2_5 = "A2 ТЕТРАДЬ"
level2_5_coord = "A2"


# level_3
level3_1 = ("    1 2 3 4 5 6\n", "A   в ы о р и ц", "B   щ а м т у с", "C   л ш г и к ы", "D   ш ч к д н з", "E   ь а р а ф ж", "F   з п м р у к")
level3_2 = ("    1 2 3 4 5 6\n", "A   а п р и м о", "B   в щ е с я р", "C   ц к в с и ч", "D   т у а с р о", "E   а и п к а л", "F   г р а к е ы")
level3_3 = ("    1 2 3 4 5 6\n", "A   п т р е к г", "B   л а т ц к ч", "C   ж д л а и м", "D   х е и в н а", "E   я ь н е и н", "F   в о г л щ х")
level3_4 = ("    1 2 3 4 5 6\n", "A   с л к д о с", "B   т е з о р р", "C   а д т н а я", "D   д и м ч п в", "E   ъ й с ь ы о", "F   ц а х ц ж ю")
level3_5 = ("    1 2 3 4 5 6\n", "A   о в к л у й", "B   н к а с р я", "C   а т с т а м", "D   п е о м е э", "E   р и н и х р", "F   л к ы ю с ь")

ans_level3_1 = "F2 ПАРАДИГМА"
level3_1_coord = "F2"
ans_level3_2 = "E4 КАЛОРИЯ"
level3_2_coord = "E4"
ans_level3_3 = "D4 ВНИМАНИЕ"
level3_3_coord = "D4"
ans_level3_4 = "C2 ДЕЗОДОРАНТ"
level3_4_coord = "C2"
ans_level3_5 = "D3 ОСТАНОВКА"
level3_5_coord = "D3"


# всё
lvls_1 = [level1_1,level1_2,level1_3,level1_4,level1_5]
lvls_ans_1 = [ans_level1_1, ans_level1_2, ans_level1_3,ans_level1_4,ans_level1_5]
coordinates_1 = [level1_1_coord,level1_2_coord,level1_3_coord,level1_4_coord,level1_5_coord]

lvls_2 = [level2_1,level2_2,level2_3,level2_4,level2_5]
lvls_ans_2 = [ans_level2_1,ans_level2_2,ans_level2_3,ans_level2_4,ans_level2_5]
coordinates_2 = [level2_1_coord,level2_2_coord,level2_3_coord,level2_4_coord,level2_5_coord]

lvls_3 = [level3_1,level3_2,level3_3,level3_4,level3_5]
lvls_ans_3 = [ans_level3_1,ans_level3_2,ans_level3_3,ans_level3_4,ans_level3_5]
coordinates_3 = [level3_1_coord,level3_2_coord,level3_3_coord,level3_4_coord,level3_5_coord]


# баллы
points_all = []







# выбор
def choice():
    print("Теперь выбери: идем дальше или в главное меню?")
    answer1 = input("1. Дальше 2. В главное меню: ")
    if answer1 == "2":
        menu_1()
    elif answer1 == "1":
        print("Продолжай игру!")
    else:
        print("Нет такого варинта ответа.")
        print("1. Дальше 2. В главное меню ")
        while answer1 != "1" or answer1 != "2":
            answer1 = input("Попробуй снова: ")
            if answer1 == "2":
                menu_1()
                break
            elif answer1 == "1":
                print("Продолжай игру!")
                break








# 1 уровень
def level_1(point1):
    print("""

                                                        LEVEL 1

                                 
          """  )
    while True:
        square_for_lvl_1 = random.choice(lvls_1)
        square_for_lvl_1_index = lvls_1.index(square_for_lvl_1)
        square_for_lvl_1_ans = lvls_ans_1[square_for_lvl_1_index]
        square_for_lvl_1_coord = coordinates_1[square_for_lvl_1_index]
        for i in range(len(square_for_lvl_1)):
            print(square_for_lvl_1[i])
        print()
        word1 = input("Я жду твой ответ: ")
        word1 = word1.upper()
        if word1 == square_for_lvl_1_ans:
            print("Молодец! Ты угадал слово!")
            point1 += 3
        else:
            print("Неправильно. У тебя последняя попытка.")
            print()
            print("Хотите воспользоваться подсказкой?")
            ans_key = input("1.Да, 2.Нет: ")
            if ans_key == "1":
                print()
                print("Тогда Держи Подсказку!")
                print("Координата первой буквы:",square_for_lvl_1_coord)
                point1 += 1
            elif ans_key == "2":
                print()
                print("Продолжай игру.")
                point1 += 2
            else:
                print("Нет такого варианта ответа.")
                while ans_key != "1" or ans_key != "2":
                    ans_key = input("Попробуй снова: ")
                    if ans_key == "1":
                        print()
                        print("Тогда Держи Подсказку!")
                        print("Координата первой буквы:",square_for_lvl_1_coord)
                        point1 += 1
                        break
                    elif ans_key == "2":
                        print()
                        print("Продолжай игру.")
                        point1 += 2
                        break
            word2 = input("Попробуй еще раз: ")
            word2 = word2.upper()
            if word2 == square_for_lvl_1_ans:
                print()
                print("Молодец! Ты угадал слово! Продолжай.")
            else:
                print()
                print("Мне очень жаль. Ты проиграл.")
                sys.exit()
        del lvls_1[square_for_lvl_1_index]
        del lvls_ans_1[square_for_lvl_1_index]
        del coordinates_1[square_for_lvl_1_index]
        print()
        print("У тебя уже", point1, "балла(ов)!")
        choice()
        if len(lvls_1) == 0:
            break
    points_all.append(point1)
    level_2(0)
    












        


# 2 уровень
def level_2(point2):
    print("""

                                                        LEVEL 2

                                 
          """  )
    while True:
        square_for_lvl_2 = random.choice(lvls_2)
        square_for_lvl_2_index = lvls_2.index(square_for_lvl_2)
        square_for_lvl_2_ans = lvls_ans_2[square_for_lvl_2_index]
        square_for_lvl_2_coord = coordinates_2[square_for_lvl_2_index]
        for e in range(len(square_for_lvl_2)):
            print(square_for_lvl_2[e])
        print()
        word3 = input("Твой ответ: ")
        word3 = word3.upper()
        if word3 == square_for_lvl_2_ans:
            print("Молодец! Ты угадал слово.")
            point2 += 4
        else:
            print("Неправильно. У тебя последняя попытка.")
            print()
            print("Хотите воспользоваться подсказкой?")
            ans_key = input("1.Да, 2.Нет: ")
            if ans_key == "1":
                print()
                print("Тогда Держи Подсказку!")
                print("Координата первой буквы:",square_for_lvl_2_coord)
                point2 += 2
            elif ans_key == "2":
                print()
                print("Продолжай игру.")
                point2 += 3
            else:
                print("Нет такого варианта ответа.")
                while ans_key != "1" or ans_key != "2":
                    ans_key = input("Попробуй снова: ")
                    if ans_key1 == "1":
                        print("Тогда Держи Подсказку!")
                        print("Координата первой буквы:",square_for_lvl_2_coord)
                        point2 += 2
                        break
                    elif ans_key == "2":
                        print()
                        print("Продолжай игру.")
                        point2 += 3
                        break
            word4 = input("Попробуй еще раз: ")
            word4 = word4.upper()
            if word4 == square_for_lvl_2_ans:
                print()
                print("Молодец! Ты угадал слово! Продолжай.")
            else:
                print()
                print("Мне очень жаль. Ты проиграл.")
                sys.exit()
        del lvls_2[square_for_lvl_2_index]
        del lvls_ans_2[square_for_lvl_2_index]
        del coordinates_2[square_for_lvl_2_index]
        print()
        if len(lvls_1) < 3:
            print("У тебя уже", point2+points_all[0], "балла(ов)!")
        else:
            print("У тебя уже", point2, "балла(ов)!")
        choice()
        if len(lvls_2) == 0:
            break
    points_all.append(point2)
    level_3(0)
























# 3 уровень
def level_3(point3):
    print("""

                                                        LEVEL 3

                                 
          """  )
    while True:
        square_for_lvl_3 = random.choice(lvls_3)
        square_for_lvl_3_index = lvls_3.index(square_for_lvl_3)
        square_for_lvl_3_ans = lvls_ans_3[square_for_lvl_3_index]
        square_for_lvl_3_coord = coordinates_3[square_for_lvl_3_index]
        for p in range(len(square_for_lvl_3)):
            print(square_for_lvl_3[p])
        print()
        word5 = input("Твой ответ: ")
        word5 = word5.upper()
        if word5 == square_for_lvl_3_ans:
            print("Молодец! Ты угадал слово.")
            point3 += 5
        else:
            print("Неправильно. У тебя последняя попытка.")
            print()
            print("Хотите воспользоваться подсказкой?")
            ans_key = input("1.Да, 2.Нет: ")
            if ans_key == "1":
                print()
                print("Тогда Держи Подсказку!")
                print("Координата первой буквы:",square_for_lvl_3_coord)
                point3 += 3
            elif ans_key == "2":
                print()
                print("Продолжай игру.")
                point3 += 4
            else:
                print("Нет такого варианта ответа.")
                while ans_key != "1" or ans_key != "2":
                    ans_key = input("Попробуй снова: ")
                    if ans_key == "1":
                        print("Тогда Держи Подсказку!")
                        print("Координата первой буквы:",square_for_lvl_3_coord)
                        point3 += 3
                        break
                    elif ans_key == "2":
                        print()
                        print("Продолжай игру.")
                        point3 += 4
                        break
            word6 = input("Попробуй еще раз: ")
            word6 = word6.upper()
            if word6 == square_for_lvl_3_ans:
                print()
                print("Молодец! Ты угадал слово! Продолжай.")
            else:
                print()
                print("Мне очень жаль. Ты проиграл.")
                sys.exit()
        del lvls_3[square_for_lvl_3_index]
        del lvls_ans_3[square_for_lvl_3_index]
        del coordinates_3[square_for_lvl_3_index]
        print()
        if len(lvls_1) < 3:
            if len(lvls_2) < 3: 
                points_all_sum = points_all[0]+points_all[1]+point3
                print("У тебя уже", points_all_sum, "балла(ов)!")
            else:
                points_all_sum = points_all[0]+point3
                print("У тебя уже", points_all_sum, "балла(ов)!")
        else:
            if len(lvls_2) < 3: 
                points_all_sum = points_all[0]+point3
                print("У тебя уже", points_all_sum, "балла(ов)!")
            else:
                points_all_sum = point3
                print("У тебя уже", points_all_sum, "балла(ов)!")
        choice()
        if len(lvls_3) == 0:
            break
    
    #################################################################
        
    print()
    print("А дальше уже некуда! Уровни окончены!")
    print("И за всю игру вы набрали",points_all_sum,"балла(ов)!")
    print("Теперь выбери: выйти из игры или в главное меню?")
    game_end = input("1. Выход 2. В главное меню: ")
    if game_end == "1":
        print("До встречи!")
        sys.exit()
    elif game_end == "2":
        menu_1()
    else:
        print("Нет такого варианта ответа.")
        while game_end != "1" or game_end != "2":
            game_end = input("Попробуй снова: ")
            if game_end == "1":
                print("До встречи!")
                sys.exit()
                break
            elif game_end == "2":
                menu_1()
                break
    

    











# меню
def menu_1():
    print("Теперь выбери уровень сложности:")
    level = input("1. Easy, 2. Normal, 3. Hard: ")
    if level == "1":
        level_1(0)
    elif level == "2":
        level_2(0)
    elif level == "3":
        level_3(0)
    else:
        print("Нет такого варианта ответа.")
        while level != "1" or level != "2" or level != "3":
            level = input("Попробуй еще раз: ")
            if level == "1":
                level_1(0)
                break
            elif level == "2":
                level_2(0)
                break
            elif level == "3":
                level_3(0)
                break
















# Программа
print(
"""
                                                         Привет. Давай сыграем в игру.
                Я дам тебе квадрат, состоящий из букв. В нем спрятано 1 слово.
                Первый столбец и верхняя строчка это координаты.
                Размер квадрата зависит от уровня сложности:
                Easy - 4x4, Normal - 5x5, Hard - 6x6.

                Для начала расскажу тебе правила:
                Ты вводишь сначала координату, с которого начинается слово (например, A1).
                Затем ты пишешь само слово, которое ты нашел
                (через пробел после координат).
                Слова состоят не менее чем из 4-х букв.
                Слово не обязательно расположено на одной прямой.
    
                У тебя максимум 1 ошибка за квадрат слов. Так что хорошенько подумай.
                Для каждого уровня сложности начисляется определенное кол-во баллов.
                Easy - 3 балла, Normal - 4 балла, Hard - 5 балла.
                                
                Так же ты можешь воспользоваться подсказкой по желанию.
                После твоей первой ошибки тебе будет предложена подсказка (по желанию).
                Если ты воспользуешься подсказкой, то ты заработаешь на 2 балла ниже,
                т.к. подсказка предлагается уже после ошибки.
                Если же ты просто ошибешься, без использования подсказки, ты заработаешь лишь на 1 балл меньше.

                                                        Привести пример? 

""")
primer = input("1. Да 2. Нет: ")
if primer == "1":
    print("Пример. Квадрат слов:")
    print("    1 2 3\n")
    print("A   н о р")
    print("B   с й о")
    print("C   о к ф")
    print("Ответ: B2 сок")
    print("Расшифровка: начинаем с буквы на месте B2.")
    print("Спускаемся на букву ниже, а затем на букву вправо.")
    print("И получается слово 'сок'.")
    print("И пишем его через пробел после координат.")
    print("Вот так ищи слова.")
    print()
elif primer == "2":
    print("Хорошо. Тогда начем игру!")
else:
    print("Нет такого варианта ответа.")
    while primer != "1" or primer != "2":
        primer = input("Попробуй еще раз: ")
        if primer == "1":
            print("Пример. Квадрат слов:")
            print("    1 2 3\n")
            print("A   н о р")
            print("B   с й о")
            print("C   о к ф")
            print("Ответ: B2 сок")
            print("Расшифровка: начинаем с буквы на месте B2.")
            print("И через пробел пишем слово 'сок'")
            print("Вот так ищи слова.")
            print()
            break
        elif primer == "2":
            print("Хорошо. Тогда начем игру!")
            break
menu_1()
