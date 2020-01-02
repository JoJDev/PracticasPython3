
def factorial(number: int):
    if (number == 0):
        return 1;
    else:
        return number * factorial(number-1);


def run():
    print("\t\tFacorial");

    num = int(input("escribe un numero a factorizar: "));

    print("el factorial de ",num," es: " + str(factorial(num)))



if __name__ == "__main__":
    run();