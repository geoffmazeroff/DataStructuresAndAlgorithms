class TrieNode:
    def __init__(self):
        self.children = {}  # Hash table of char->TrieNode

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        current_node = self.root
        
        # Traverse the trie character by character until the character is
        # missing, or we're done with the word.
        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                return None

        return current_node

    def insert(self, word):
        current_node = self.root

        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                new_node = TrieNode()
                current_node.children[char] = new_node
                current_node = new_node

        # Once inserted, put an end-marker in place
        current_node.children["*"] = None

    def collect_all_words(self, node=None, word="", words=[]):
        current_node = node or self.root

        for key, child_node in current_node.children.items():
            # Reached the end of a word
            if key == "*":
                words.append(word)
            # Not done; recursively keep going
            else:
                self.collect_all_words(child_node, word + key, words)

        return words

    def auto_complete(self, prefix):
        current_node = self.search(prefix)
        if not current_node: 
            return None

        # BUG: the book just does collect_all_words(current_node)
        # but if collect_all_words has been called before, somehow the previous
        # set of collected words persists! Sending in an empty array fixed it.
        return self.collect_all_words(current_node, prefix, [])

    def traverse(self, node=None):
        # Note: This code is from the book, and I don't really see how it's
        # helpful in understanding whether the trie is set up correctly. :-(
        current_node = node or self.root

        for key, child_node in current_node.children.items():
            print("key={0}, node={1}".format(key, child_node))
            if key != "*": self.traverse(child_node)

    def autocorrect(self, word):
        current_node = self.root
        word_found_so_far = ""
        
        for char in word:
            if current_node.children.get(char):
                word_found_so_far += char
                current_node = current_node.children.get(char)
            else:
                # BUG: The solution in the book (word_found_so_far + self.collect_all_words(current_node[0]))
                # doesn't even meet the requirements of the exercise. It also returns the wrong results.
                all_suffixes = self.collect_all_words(current_node, "", [])
                to_return = []
                for x in all_suffixes:
                    to_return.append(word_found_so_far + x)
                return to_return

        return word

# Part 1 -- put words in the trie
print("=== Building trie...")
wordlist = Trie()
wordlist.insert("get")
wordlist.insert("go")
wordlist.insert("got")
wordlist.insert("gotten")
wordlist.insert("hall")
wordlist.insert("ham")
wordlist.insert("hammer")
wordlist.insert("hill")
wordlist.insert("zebra")

# Part 2 -- show all words
print("=== All the words...")
print(wordlist.collect_all_words())

# Part 3 -- autocomplete on "go"
print("=== All words starting with 'go'...")
print(wordlist.auto_complete("go"))

# Part 4 -- autocorrect
print("=== Autocorrecting 'gox'...")
print(wordlist.autocorrect("gox"))