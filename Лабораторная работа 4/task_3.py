def delete(list_, index=None):
    if index == None:   # Условие, при недостаточных входных данных
        return list_[:-1]
    else:
        if index == -1: # Условие для отрицательного значения индекса
            return list_[:index]
        else:
            return list_[:index] + list_[(index + 1):] # Использование слайсирования
print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]