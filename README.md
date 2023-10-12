# DNA Replication Simulator

This repository contains a Python-based DNA replication simulator. The simulator includes classes to represent DNA, DNA generators, a nucleus, and polymerase.

## Classes

### Main.py

This script demonstrates the simulation of DNA replication using the provided classes. It generates DNA data, replicates DNA in the nucleus using mitosis and meiosis, and prints the resulting DNA strands.

### DNA.py

This module defines the `DNA` and `DNA_Generator` classes. The `DNA` class represents a DNA strand and provides methods to manipulate DNA strands, while the `DNA_Generator` class generates DNA sequences.

#### `DNA` class

- `__init__(self, data, random=False)`: Initializes a DNA instance with given data or generates random data if specified.
- `get_complement_strand(self, dna_sequence)`: Returns the complementary strand of a given DNA sequence.
- `get_helix(self)`: Returns the helix representation of the DNA.

#### `DNA_Generator` class

- `__init__(self, seed=69)`: Initializes a DNA generator with an optional seed for randomization.
- `gen_dna(self)`: Generates a DNA sequence using predefined codons and start/end codons.
- `gen_data(self, n_gen=23)`: Generates a list of DNA sequences using `gen_dna`.

### Polimerase.py

This module defines the `Polimerase` class, which represents a polymerase responsible for DNA replication through mitosis and meiosis.

#### `Polimerase` class

- `mitosis(self, helix)`: Simulates mitosis and synthesizes new DNA strands.
- `synthesize_strand(self, template_strand)`: Synthesizes a complementary DNA strand based on a template strand.
- `meiosis_1(self, helix)`: Simulates meiosis phase 1 and creates new DNA strands.
- `meiosis_2(self, helix)`: Simulates meiosis phase 2 and creates new DNA strands.

### Nucleus.py

This module defines the `Nucleus` class, which represents a nucleus containing DNA sequences and facilitates DNA replication through mitosis and meiosis.

#### `Nucleus` class

- `__init__(self, dna_list=[]))`: Initializes a nucleus with a given list of DNA sequences or generates random DNA if not provided.
- `replicate_dna(self, meiosis=False)`: Replicates DNA within the nucleus using mitosis or meiosis, based on the specified option.

## Authors

- Adrián Perera Moreno
- Álvaro Juan Travieso García

## How to Use

To use the DNA replication simulator, run the `Main.py` script. It demonstrates DNA replication through mitosis and meiosis, printing the resulting DNA strands in each phase.

```python
python Main.py
