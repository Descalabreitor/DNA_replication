from DNA import DNA, DNA_Generator
from Polimerase import Polimerase

class Nucleus:

    dna_list = []

    def __init__(self, dna_list = []):
        if len(dna_list) == 0:
            dna_gen = DNA_Generator()
            self.dna_list.extend(dna_gen.gen_data())


    def replicate_dna(self, meiosis=False):
        polimerase = Polimerase()
        dna_list_1 = []
        dna_list_2 = []
        
        for dna in self.dna_list:
            if meiosis:
                new_dna1, new_dna2 = polimerase.meiosis_1(dna.get_helice())
                new_dna3, new_dna4 = polimerase.meiosis_2(dna.get_helice())
                dna_list_1.append(DNA(''.join([new_dna1, new_dna2])))
                dna_list_2.append(DNA(''.join([new_dna3, new_dna4])))
            else:
                new_dna1, new_dna2 = polimerase.mitosis(dna.get_helice())
                dna_list_1.append(DNA(new_dna1))
                dna_list_2.append(DNA(new_dna2))

        return Nucleus(dna_list_1), Nucleus(dna_list_2)
