# bloom

What is a Bloom filter?
- A space-efficient probabilistic data structure that stores a bit array created off of hashes of the data
- It doesn’t store the data itself but can be used to test membership, i.e. “Have I seen this data element before or not?”
- False negatives aren’t possible, meaning if I test membership for a data element that was part of the originally hashed set, I will always find it in the Bloom filter
- False positives are possible, meaning something can test as in the Bloom filter without being part of the originally hashed set. Fortunately you can specify the rate at which false positives occur. A lower desired false positive rate just means a larger bloom size.


