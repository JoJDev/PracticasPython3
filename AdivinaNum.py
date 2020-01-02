import random;

def run():
    numEncontrado = False;
    numAleatorio = random.randint(0,30);

    while not numEncontrado:
        number = int(input("Elige un numero del 0 al 30: "));

        if number == numAleatorio:
            print("¡Felicidades! encontraste el numero (",numAleatorio,")");
            numEncontrado = True;
        elif number < numAleatorio:
            print("El numero es mas grade");
        else:
            print("El numero es mas pequeño");

if __name__ == "__main__":
    run();