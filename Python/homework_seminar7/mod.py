
def get_new_per():
        dic = {input('Введите ФИО:'): input('Введите телефон: ')}
        return dic 
    
def get_1st_userchar():
    char1 = input('Введите первую букву Фамилии: ')
    return char1


def change_name():
        old_name = input('Введите ФИО, которые нужно изменить: ')
        new_name = input('Введите новые данные ФИО: ')
        return old_name, new_name

def change_phone():
        old_phone = input('Введите ФИО абонента: ')
        new_phone = input('Введите новый телефон: ')
        return old_phone, new_phone