from DNA import DNA_Generator
from Nucleus import Nucleus

def main():
    # Crear una instancia de DNA_Generator para generar datos de ADN
    dna_gen = DNA_Generator()

    # Generar una lista de ADN
    dna_list = dna_gen.gen_data(23)

    # Crear una instancia de Nucleus con la lista de ADN
    nucleus = Nucleus(dna_list)

    # Replicar el ADN en el núcleo mediante mitosis
    nucleus1_mitosis, nucleus2_mitosis = nucleus.replicate_dna(meiosis=False)

    # Imprimir las hebras de ADN resultantes de la mitosis
    print("Mitosis - Hebras de ADN en Núcleo 1:")
    for dna in nucleus1_mitosis.dna_list:
        print(dna.get_helice())

    print("\nMitosis - Hebras de ADN en Núcleo 2:")
    for dna in nucleus2_mitosis.dna_list:
        print(dna.get_helice())

    # Replicar el ADN en el núcleo mediante meiosis
    nucleus1_meiosis, nucleus2_meiosis = nucleus.replicate_dna(meiosis=True)

    # Imprimir las hebras de ADN resultantes de la meiosis
    print("\nMeiosis - Hebras de ADN en Núcleo 1:")
    for dna in nucleus1_meiosis.dna_list:
        print(dna.get_helice())

    print("\nMeiosis - Hebras de ADN en Núcleo 2:")
    for dna in nucleus2_meiosis.dna_list:
        print(dna.get_helice())

if __name__ == "__main__":
    main()


