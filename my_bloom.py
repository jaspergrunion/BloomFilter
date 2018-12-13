# Program to create a bloom filter

import mmh3
from bitarray import bitarray
from sklearn.model_selection import train_test_split
from math import log, log2
from utils import read_words, time_it

class myBloomFilter:
    """ Bloom filter object """
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, item):
        for i in range(self.hash_count):
            index = mmh3.hash(item, seed=i) % self.size
            self.bit_array[index] = 1
        return self.bit_array

    def __contains__(self, newitem):
        out = True
        for i in range(self.hash_count):
            index = mmh3.hash(newitem, seed=i) % self.size
            if self.bit_array[index] == 0:
                out = False
        return out

    def summary(self):
        self.view = ''.join(['1' if x else '0' for x in self.bit_array])
        self.sum = sum(self.bit_array)
        print("First 100 Bits: ", self.view[:100])
        print("Bloom size:", "{:,}".format(self.size))
        print("Hash Count:", "{:,}".format(self.hash_count))
        print("Bit sum:", "{:,}".format(self.sum))
        # print("Bit density:", "{:.4f}".format(self.sum/len(self.view)), "\n")

@time_it
def main():
    """Program to create and index a bloom filter"""

    print("BLOOM FILTER PROGRAM\n")

    terms_raw = read_words("/usr/share/dict/words")

    # Split into train, test
    terms, other_terms = train_test_split(terms_raw, test_size=0.3, random_state=1234)

    # Bloom filter parameters
    # p false positive rate, m bits, n in-sample elements, n2 out-of-sample elements, k hash functions

    p = .01
    n = len(terms)
    n2 = len(other_terms)
    m = int(-(n * (log(p))) / ((log(2)) ** 2))
    k = int(-log2(p))

    print("Desired false positive rate: ", p)
    print("Number of terms to hash: ", "{:,}".format(n))
    print("Number of out-of-sample terms: ", "{:,}".format(n2))
    print("Ideal bloom size: ", "{:,}".format(m))
    print("Ideal hash count: ", "{:,}".format(k), "\n")

    # Instantiate bloom filter
    myBloom = myBloomFilter(m, k)

    # Hash terms
    for terms_hashed, term in enumerate(terms):
        myBloom.add(term)

    myBloom.summary()

    # Check in-sample cases
    print("IN SAMPLE CASES: \n")
    false_negatives = 0
    for terms_checked, term in enumerate(terms):
        if term not in myBloom:
            print('{} IS A FALSE NEGATIVE'.format(term))
            false_negatives += 1

    print("Number of terms checked: ", "{:,}".format(terms_checked + 1))
    print("Total false negatives: ", "{:,}".format(false_negatives))
    print("False negative rate: ", "{:.4f}".format(false_negatives / (terms_checked + 1)), "\n")

    # Check out-of-sample cases
    print("OUT OF SAMPLE CASES: \n")
    false_positives = 0
    for other_terms_checked, other_term in enumerate(other_terms):
        if other_term in myBloom:
            # print('{} IS A FALSE POSITIVE'.format(other_term))
            false_positives += 1

    print("Number of terms checked: ", "{:,}".format(other_terms_checked + 1))
    print("Total false positives: ", "{:,}".format(false_positives))
    print("False positive rate: ", "{:.4f}".format(false_positives / (other_terms_checked + 1)))


if __name__ == "__main__":
    main()
