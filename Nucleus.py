from DNA_Generator import DNA_Generator
from DNA import DNA

class Nucleus:

    self.dna_list = []

    def __init__(self, dna_list = []):
        if len(dna_list) == 0:
            dna_gen = DNA_Generator()
            self.dna_list.extend(dna_gen.get_data())


    def replicate_dna(self):
        polimerasa = Polimerasa()
        dna_list_1 = []
        dna_list_2 = []
        
        for dna in self.dna_list:
            new_dna1, new_dna2 = polimerasa.replicate(dna.get_helice())
            dna_list_1.append(new_dna1)
            dna_list_2.append(new_dna2)

        return Nucleus(dna_list_1), Nucleus(dna_list_2)