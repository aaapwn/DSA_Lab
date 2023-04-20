def insertion_sort(list, last):
    """Insertion Sort"""
    isCard = False
    if type(list[0]) == str:
        list = change_card_data(list)
        isCard = True
    current = 1
    compare = 0
    while current <= last:
        hold = list[current]
        walker = current - 1
        while (walker >= 0 and hold < list[walker]):
            compare += 1
            walker -= 1
        compare += 1
        list.remove(hold)
        list.insert(walker+1, hold)
        current += 1
        if isCard:
            print(change_card_data(list))
        else:
            print(list)
    print("Comparison times :", compare)

def selection_sort(list,last):
    """Selection Sort"""
    isCard = False
    if type(list[0]) == str:
        list = change_card_data(list)
        isCard = True
    compare = 0
    current = 0
    while current < last:
        smallest = current
        walker = current + 1
        while (walker <= last):
            compare += 1
            if list[walker] < list[smallest]:
                smallest = walker
            walker += 1
        list[current], list[smallest] = list[smallest], list[current]
        compare += 1
        current += 1
        if isCard:
            print(change_card_data(list))
        else:
            print(list)
    print("Comparison times :", compare)

def bubble_sort(list, last):
    """Bubble Sort"""
    isCard = False
    if type(list[0]) == str:
        list = change_card_data(list)
        isCard = True
    compare = 0
    current = 0
    _sorted = False
    while (current <= last and not _sorted):
        walker = last
        _sorted = True
        while (walker > current):
            compare += 1
            if list[walker] < list[walker-1]:
                _sorted = False
                list[walker], list[walker-1] = list[walker-1], list[walker]
            walker -= 1
        current += 1
        if isCard:
            print(change_card_data(list))
        else:
            print(list)
    print("Comparison times :", compare)

def change_card_data(list):
    new_list = []
    # s = โพดำ, h = โพแดง, d = ข้าวหลามตัด, c = ดอกจิก
    #* number in card to int
    if type(list[0]) == str:
        for i in list:
            front = i[0] if len(i) == 2 else i[:2]
            back = i[1] if len(i) == 2 else i[2]
            if back == '♣':
                mul = 0.1
            elif back == '♦':
                mul = 0.2
            elif back == '♥':
                mul = 0.3
            elif back == '♠':
                mul = 0.4
            if front.isnumeric():
                base = int(front)
            else:
                if front == 'J':
                    base = 11
                elif front == 'Q':
                    base = 12
                elif front == 'K':
                    base = 13
                elif front == 'A':
                    base = 14
            new_list.append(base+mul)
    #* int to number in card
    else:
        for i in list:
            if str(i)[len(str(i))-1] == '1':
                back = '♣'
            elif str(i)[len(str(i))-1] == '2':
                back = '♦'
            elif str(i)[len(str(i))-1] == '3':
                back = '♥'
            elif str(i)[len(str(i))-1] == '4':
                back = '♠'
            front = int(i)
            if front > 10:
                if front == 11:
                    front = 'J'
                elif front == 12:
                    front = 'Q'
                elif front == 13:
                    front = 'K'
                elif front == 14:
                    front = 'A'
            new_list.append(str(front)+back)
    return new_list

insertion_sort([23, 78, 45, 8, 32, 56], 5)

insertion_sort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)