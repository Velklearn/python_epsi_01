#Fonction several_zeros
def several_zeros():
    list = [0] * 10
    return list
pass

#Fonction several_zeros_custom

def several_zeros_custom(nb_zeros):
    list2 = [0] * nb_zeros
    return list2
pass

#Fonction matrix

def matrix(rows, cols):
    matrice_table = [
        [0 for i in range(cols)],[0 for i in range(rows)]]
    return matrice_table

#Objet matrix

class Matrix:
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    def get_value(self, row, col):
        return self._matrix[row][col]

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        return self._matrix == other._matrix

#Fonction sort (5 points + 1 point bonus)

def my_sort(my_list: list[int]) -> list[int]:
    # Créer une copie de la liste pour ne pas modifier l'originale
    sorted_list = my_list.copy()
    n = len(sorted_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_list[j] > sorted_list[j+1]:
                # Échanger les éléments
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
    return sorted_list

#Print

if __name__ == '__main__':
    print(several_zeros())
    print(several_zeros_custom(3))
    print(matrix(3,2))
    
    m1 = Matrix(2, 3)
    m2 = Matrix(2, 3)
    print(m1 == m2)  # True
    print(m1.get_value(1, 2))  # 0
    
    my_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = my_sort(my_list)
    print("Liste originale:", my_list)
    print("Liste triée:", sorted_list)
pass