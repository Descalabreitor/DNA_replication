from DNA import DNA_Generator
from Nucleus import Nucleus

def main():
    # Crear una instancia de DNA_Generator para generar datos de ADN
    dna_gen = DNA_Generator()

    # Generar una lista de ADN
    dna_list = dna_gen.gen_data(23)

    # Crear una instancia de Nucleus con la lista de ADN
    nucleus = Nucleus(dna_list)

    # Replicar el ADN en el núcleo
    nucleus1, nucleus2 = nucleus.replicate_dna()

    # Imprimir las hebras de ADN resultantes
    print("Hebras de ADN en Núcleo 1:")
    for dna in nucleus1.dna_list:
        print(dna.get_helice())

    print("\nHebras de ADN en Núcleo 2:")
    for dna in nucleus2.dna_list:
        print(dna.get_helice())

if __name__ == "__main__":
    main()
