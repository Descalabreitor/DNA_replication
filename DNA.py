from DNA_Generator import DNA_Generator

class DNA:

    def __init__(self, data="", random=False):
        if random:
            self.data = DNA_Generator().gen_dna()
        else:
            self.data = data
        self.helice = [self.data, self.calcular_hebra_complementaria(self.data)]

    def calcular_hebra_complementaria(self, secuencia_adn):
        complemento = {"A": "T", "T": "A", "C": "G", "G": "C"}
        hebra_complementaria = ''.join(complemento[base] for base in reversed(secuencia_adn))
        return hebra_complementaria

    def get_helice(self):
        return self.helice