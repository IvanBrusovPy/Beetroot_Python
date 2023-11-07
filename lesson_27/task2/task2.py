from hash_table import HashTable


class HashTableUpgrade(HashTable):
    def __contains__(self, value):
        return value in self.data

    def __len__(self):
        return len(list(filter(lambda x: x is not None, self.slot)))


if __name__ == "__main__":
    H = HashTableUpgrade()
    H[54] = "cat"
    H[26] = "dog"
    H[93] = "lion"
    H[17] = "tiger"
    H[77] = "bird"
    H[31] = "cow"
    H[44] = "goat"
    H[55] = "pig"
    H[20] = "chicken"

    print(len(H))
    print("bird" in H)
