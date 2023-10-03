class Polimerasa:
    def replicate(self, helice):
        new_helice_1 = self.synthesize_strand(helice[0])
        new_helice_2 = self.synthesize_strand(helice[1])
        return new_helice_1, new_helice_2

    def synthesize_strand(self, template_strand):
        complemento = {"A": "T", "T": "A", "C": "G", "G": "C"}
        new_strand = ''.join(complemento[base] for base in template_strand)
        return new_strand
