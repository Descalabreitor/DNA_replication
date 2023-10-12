class Polimerase:
    def mitosis(self, helix):
        new_strand_1 = self.synthesize_strand(helix[0])
        new_strand_2 = self.synthesize_strand(helix[1])
        new_helix_1 = [helix[0], new_helix_1]
        new_helix_2 = [helix[1], new_strand_2]
        return new_helix_1, new_helix_2

    def synthesize_strand(self, template_strand):
        complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
        new_strand = ''.join(complement[base] for base in template_strand)
        return new_strand

    def meiosis_1(self, helix):
        len_helix = len(helix[0])
        new_helix_1 = helix[0][:len_helix // 2] + helix[1][:len_helix // 2]
        new_helix_2 = helix[1][:len_helix // 2] + helix[0][:len_helix // 2]
        return new_helix_1, new_helix_2

    def meiosis_2(self, helix):
        len_helix = len(helix[0])
        new_helix_1 = helix[0][len_helix // 2:] + helix[1][len_helix // 2:]
        new_helix_2 = helix[1][len_helix // 2:] + helix[0][len_helix // 2:]
        return new_helix_1, new_helix_2