class Polimerasa:
    def mitosis(self, helice):
        new_strand_1 = self.synthesize_strand(helice[0])
        new_strand_2 = self.synthesize_strand(helice[1])
        new_helice_1 = [helice[0], new_helice_1]
        new_helice_2 = [helice[1], new_strand_2]
        return new_helice_1, new_helice_2

    def synthesize_strand(self, template_strand):
        complemento = {"A": "T", "T": "A", "C": "G", "G": "C"}
        new_strand = ''.join(complemento[base] for base in template_strand)
        return new_strand

    def meiosis_1(self, helice):
        len_helice = len(helice[0])
        new_helice_1 = helice[0][:len_helice // 2] + helice[1][:len_helice // 2]
        new_helice_2 = helice[1][:len_helice // 2] + helice[0][:len_helice // 2]
        return new_helice_1, new_helice_2

    def meiosis_2(self, helice):
        len_helice = len(helice[0])
        new_helice_1 = helice[0][len_helice // 2:] + helice[1][len_helice // 2:]
        new_helice_2 = helice[1][len_helice // 2:] + helice[0][len_helice // 2:]
        return new_helice_1, new_helice_2