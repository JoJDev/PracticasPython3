
def operacionesConListas():
    lista1 = [0,12,3,6,6,1.2];
    lista2 = ["Carlos", "Pepe", "Juan", "Maria"];

    lista3 = lista1 + lista2;
    print(lista3);

    lista4 = [4,23]
    lista5 = lista4 * 8;
    print(lista4,"\n\b",lista5);

    del lista1[0];
    lista1.append(4585);

    print(lista1);

def promedioTemp(temps:list()):
    totalTemp = 0;

    for temp in temps:
        totalTemp += temp;
    
    return totalTemp / len(temps);


def main():
    temps = [21,15,25,21,10,25,29,30,30,26];
    
    amigos = list();
    amigos.append("Pedro");
    amigos.append("Jose");
    amigos.append("Enrique");

    print(amigos);

    print(promedioTemp(temps));

    operacionesConListas();

    return 0;

if __name__ == "__main__":
    main();

    