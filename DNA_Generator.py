import numpy as np

from DNA import DNA

class DNA_Generator:

    codons_list =  ["ATG", "TTT", "TTC", "TTA", "TTG", "TCT", "TCC", "TCA", "TCG",
                         "TAT", "TAC", "TGT", "TGC", "TGG", "CTT", "CTC", "CTA", "CTG",
                         "CCT", "CCC", "CCA", "CCG", "CAT", "CAC", "CAA", "CAG", "CGT",
                         "CGC", "CGA", "CGG", "ATT", "ATC", "ATA", "ATG", "ACT", "ACC",
                         "ACA", "ACG", "AAT", "AAC", "AAA", "AAG", "AGT", "AGC", "AGA",
                         "AGG", "GTT", "GTC", "GTA", "GTG", "GCT", "GCC", "GCA", "GCG",
                         "GAT", "GAC", "GAA", "GAG", "GGT", "GGC", "GGA", "GGG"]


    start_codon = "ATG"
    end_codons = ["TAA", "TAG", "TGA"]

    def __init__(self, dna_len=12):
        if dna_len % 3 != 0:
            raise ValueError("dna_len must be a multiple of 3")
        self.dna_len = dna_len

    def gen_dna(self):
        data =  ''.join(np.random.choice(self.codons_list) for _ in range(self.dna_len // 3))
        return DNA(''.join([self.start_codon, data, np.random.choice(self.end_codons)]))
    
    def gen_data(self, n_gen=23):
        return [self.gen_dna() for _ in range(n_gen)]
