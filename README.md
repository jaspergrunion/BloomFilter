# Bloom

What is a Bloom filter?
- A space-efficient probabilistic data structure that stores a bit array created off of hashes of the data
- It doesn’t store the data itself but can be used to test membership, i.e. “Have I seen this data element before or not?”
- False negatives aren’t possible, meaning if I test membership for a data element that was part of the originally hashed set, I will always find it in the Bloom filter
- False positives are possible, meaning something can test as in the Bloom filter without being part of the originally hashed set. Fortunately you can specify the rate at which false positives occur. A lower desired false positive rate just means a larger bloom size.

Parameters: 
- m: bloom size
- k: # of hash functions
- n: number of data elements to hash
- p: desired false positive rate
- Ideal m: -(n * (log(p))) / ((log(2)) ** 2)
- Ideal k: -log2(p)

Full overview in "Bloom Filters in Python".pptx

Python Files:
- my_bloom.py: defines a bloom object class in Python. Also contains a main method for hashing /usr/share/dict/words into it and checking for out of sample membership
- utils.py: includes two utility functions, one to read lines from a file into a list of words, the other to time the main function

```
---------------
BLOOM FILTER PROGRAM

Desired false positive rate:  0.01
Number of terms to hash:  165,120
Number of out-of-sample terms:  70,766
Ideal bloom size:  1,582,684
Ideal hash count:  6 

First 100 Bits:  1100100010011111100001000000101100001100000101011011110001101111101100110111101111011010001110000011
Bloom size: 1,582,684
Hash Count: 6
Bit sum: 735,698
Bit density: 0.4648 

IN SAMPLE CASES: 

Number of terms checked:  165,120
Total false negatives:  0
False negative rate:  0.0000 

OUT OF SAMPLE CASES: 

Number of terms checked:  70,766
Total false positives:  725
False positive rate:  0.0102
---------------
Elaspsed time: 3.3934684690029826 seconds

```



