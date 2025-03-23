import numpy

def gauss_elimination_detailed(A, b):
    """
        A: Матрица коэффициентов.
        b: Вектор свободных членов.
        x: Решение системы линейных уравнений.
    """
    condition = True
    n = len(b)  # Размерность системы уравнений

    # Объединяем матрицу A и вектор b в расширенную матрицу
    Ab = numpy.concatenate((A, b.reshape(-1, 1)), axis=1)
    print("Исходная расширенная матрица:\n", Ab)

    # Прямой ход
    for i in range(n):

        if condition:
        # Поиск максимального по модулю значения
            abs_values = numpy.abs(Ab[i:, i])
        # Преобразуем индекс среза в индекс матрицы
            max_abs_index = numpy.argmax(abs_values)
        # Преобразуем индекс относительно среза в индекс относительно всей матрицы
            max_abs_index += i
        # Меняем местами строки i и max_abs_index
            if max_abs_index != i:
            # Меняем местами строки i и max_abs_index
                Ab[[i, max_abs_index]] = Ab[[max_abs_index, i]]
                print(f"Меняем строки {i+1} и {max_abs_index+1}")
                print(f"максимум абсолютных значений в строке {abs_values} и индекс максимум знач {max_abs_index}")

        # Поиск ненулевого элемента в столбце для избежания деления на ноль (частичный выбор ведущего элемента)
        if numpy.isclose(Ab[i, i], 0):
            for k in range(i + 1, n):
                if not numpy.isclose(Ab[k, i], 0):
                    # Меняем местами строки i и k
                    Ab[[i, k]] = Ab[[k, i]]
                    print(f"\nМеняем строки {i+1} и {k+1}:\n", Ab) # нумерация строк с 1
                    break # после перестановки, переходим к следующему шагу
            else:
                print("Матрица вырождена, решение может быть неоднозначным или отсутствовать.")
                return None # Матрица вырождена

        # Обнуляем элементы под ведущим элементом
        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, :] = Ab[j, :] - factor * Ab[i, :] # Вычитаем из строки j строку i, умноженную на factor
            print (f"первый {Ab[j, i]} второй {Ab[i, i]}")
            print(f"\nВычитаем из строки {j+1} строку {i+1}, умноженную на {factor:.4f}:\n", Ab)

    # Обратный ход
    x = numpy.zeros(n)  # создаем вектор решения
    for i in range(n - 1, -1, -1):  # идем с конца матрицы вверх
        x[i] = Ab[i, n]  # Значение из последнего столбца (b)
        for j in range(i + 1, n):  # вычитаем уже известные значения x[j]
            x[i] -= Ab[i, j] * x[j]
        x[i] = x[i] / Ab[i, i] # Делим на диагональный элемент
        print(f"x[{i+1}]: Х* = {x[i]} ")

    print("\nМатрица после обратного хода (упрощенная для понимания решения):\n", Ab) # выводим финальную матрицу

    numpy.set_printoptions(precision=15)  # Точность +15

    # Умножаем A на x* = B ----- это (b*)
    B = numpy.dot(A, x)
    print("Результат перемножения A на x* (вектор b*):\n", B)

    # Разность b и B (b*)
    r = b - B
    print("b-B = r: ",r)

    # Считаем ||r||1
    sum_of_coefficients_r = numpy.sum(r)
    print("||r||1 = ", sum_of_coefficients_r)

    # Находим индекс ||r||∞
    vector_r = numpy.abs(r)
    max_index_r = numpy.argmax(vector_r)
    # Получаем максимальное значение по индексу
    max_value_r = r[max_index_r]
    print("||r||∞ = ", max_value_r)

# Для 1 нормы

    # Считаем vector x* - x
    X = x - c
    print("vector x* - x = ", X)

    # Считаем ∆(x*)1
    sum_of_coefficients_X = numpy.sum(X)
    print("∆(x*) = ", sum_of_coefficients_X)

    # Считаем ||b||1
    sum_of_coefficients_b = numpy.sum(b)
    print("||b||1 = ", sum_of_coefficients_b)

    # Считаем ||x||1
    sum_of_coefficients_c = numpy.sum(c)
    print("||x||1 = ", sum_of_coefficients_c)

    δx1 = sum_of_coefficients_X / sum_of_coefficients_c
    δb1 = sum_of_coefficients_r / sum_of_coefficients_b

    print("δ(x*)1 = ", δx1)
    print("δ(b*)1 = ", δb1)

    v1 = δx1/δb1
    print("v(A)1 ≥ ", v1)

# Для ∞ нормы

    #Считаем ∆(x*)∞
    # Находим индекс максимального значения ∆(x*)∞
    vector_X = numpy.abs(X)
    max_index_X = numpy.argmax(vector_X)
    # Получаем максимальное значение по индексу
    max_value_X = X[max_index_X]
    print("∆(x*)∞ = ", max_value_X)

    #Считаем ||x||∞
    # Находим индекс максимального значения x
    vector_c = numpy.abs(c)
    max_index_c = numpy.argmax(vector_c)
    # Получаем максимальное значение по индексу
    max_value_c = c[max_index_c]
    print("||x||∞ = ", max_value_c)

    # Считаем ||b||∞
    # Находим индекс максимального значения x
    vector_b = numpy.abs(b)
    max_index_b = numpy.argmax(vector_b)
    # Получаем максимальное значение по индексу
    max_value_b = b[max_index_b]
    print("||b||∞ = ", max_value_b)

    δx2 = max_value_X / max_value_c
    δb2 = max_value_r / max_value_b

    print("δ(x*)∞ = ", δx2)
    print("δ(b*)∞ = ", δb2)

    v2 = δx2/δb2
    print("v(A)∞ ≥ ", v2)

    return x

if __name__ == "__main__":

    A = numpy.array([[167.94, 32.67, -24.925, 60.272],
                  [-11.136, 6.434, 1.407, 10.296],
                  [1174.18, 228.69, -174.275, 421.904],
                  [27.965, 0, -3.995, 0.999],])

    b = numpy.array([-9.913, -28.789, -70.191, 16.979])

    c = numpy.array([1, -5, 3, 1])

    print("Матрица коэффициентов A:\n", A)
    print("Вектор свободных членов b:\n", b)

    x = gauss_elimination_detailed(A.copy(), b.copy())  # делаем копию

    if x is not None:
        print("\nРешение системы уравнений:\n", x)
    else:
        print("\nСистема не имеет решения или решение неоднозначно.")
