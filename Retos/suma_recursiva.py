
def sumaRecursiva(a: int, b: int):
    if b <= 0:
        return a;
    else:
        return sumaRecursiva(a + 1, b - 1);

def main():
    print("Suma recursiva");

    while True:
    # print("la suma recursiva de 5 + 8 es: " + str(sumaRecursiva(5,8)));
        a = input("Ingresa el primer num o s para salir: ");
        b = input("Ingresa el segundo num o s para salir: ");

        try:
            print("el resultado de {} + {} es: {}".format(a, b, sumaRecursiva(int(a), int(b))));    
        except RecursionError as eRE:
            print("Error: muy grande el 2do numero: " + str(eRE));
            break;
        except ValueError as eVE:
            break;
            
    



if __name__ == "__main__":
    main();