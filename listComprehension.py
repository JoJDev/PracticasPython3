if __name__ == '__main__':
    pares = [];
    for num in range(1,31):
        if num % 2 == 0:
            pares.append(num);

    print(pares);

    paresComp = [num for num in range(1,31) if num % 2 == 0];

    print(paresComp);

    cuadrados = {};
    for num in range(1,31):
        cuadrados[num] = num**2;

    print(cuadrados);

    cuadradosComp = {num: num**2 for num in range(1,31)};

    print(cuadradosComp);