from tree import TreeNode, Tree


class TrieNode(TreeNode):
    def __init__(self, value):
        assert type(value)==str, "Trie nodes accept characters only!!"
        self.parent = None
        self.data = value
        self.children = {}
        self.is_word = False

    def get_characters(self):
        return self.children.keys()

    def get_children(self):
        return list(self.children.values())

    def get_child(self, ch):
        try:
            return self.children[ch]
        except KeyError:
            return ""

    def get_parent(self):
        return self.parent

    def set_child(self, ch, new_node):
        self.children[ch] = new_node
        new_node.parent = self
    
    def has_no_children(self):
        return self.children == {}

    def __repr__(self):
        return "TrieNode({})".format(self.data)

    def represent_data(self):
        if self.is_word:
            return self.data + ' ✓'
        else:
            return self.data



class Trie(Tree):
    def __init__(self):
        self.root = TrieNode('')
        self.root.data = "ROOT"
        self.nodes_count = 1


    ############################## LENGTH ##############################
    def __len__(self):
        return self.nodes_count


    ############################## FIND ##############################
    def _follow_path(self, word):
        curr_node = self.root
        while(word):
            ch = word[0]
            child = curr_node.get_child(ch)
            #'}' is used to break the following if-condition
            child_data = child.get_data() if child else "}"
            if child_data == word[:len(child_data)] \
                or child_data[:len(word)] == word:
                word = word[len(child_data):]
                curr_node = child
            else:
                break
        return curr_node, word


    def __contains__(self, word):
        assert type(word) == str, \
        "Can't find {} since tries contain only characters!!".format(type(word))
        last_node, remaining_word = self._follow_path(word)
        return remaining_word == "" and last_node.is_word


    def has_substring(self, substr):
        assert type(substr) == str, \
        "Can't find {} since tries have only characters!!".format(type(substr))
        last_node, remaining_substr = self._follow_path(substr)
        return remaining_substr == ""


    ############################## INSERTION ##############################
    def insert(self, word):
        assert type(word) == str, "You can insert String objects only!!"
        assert len(word) > 0, "You can't insert any empty String!!"
        last_node, remaining_word = self._follow_path(word)
        curr_node = last_node
        for ch in remaining_word:
            child = TrieNode(ch)
            curr_node.set_child(ch, child)
            self.nodes_count += 1
            curr_node = child
        curr_node.is_word = True


    ############################## REMOVE ##############################
    def remove(self, word):
        assert type(word) == str, "You can remove String objects only!!"
        last_node, remaining_word = self._follow_path(word)
        # if word is found, clear it
        if remaining_word == "":
            curr_node = last_node
            if curr_node.is_word:
                curr_node.is_word = False
            while(not curr_node.is_word and curr_node.has_no_children()):
                ch = curr_node.get_data()
                parent = curr_node.get_parent()
                del parent.children[ch]
                self.nodes_count -= 1
                curr_node = parent






    ######################### AUTO-COMPLETION #########################
    def __get_candidates(self, start_node, prefix):
        output = []
        new_prefix = prefix.copy()
        new_prefix += start_node.get_data()
        if start_node.is_word:
            output.append("".join(new_prefix))
        # iterate over children
        for child in start_node.get_children():
            output.extend( self.__get_candidates(child, new_prefix) )
        return output

    def auto_complete(self, prefix=''):
        assert type(prefix) == str, "A character-sequence is expected!!"
        start_node = self.root
        # parse the prefix
        for ch in prefix:
            if ch not in start_node.get_characters():
                return []
            start_node = start_node.get_child(ch)
        # get candidates starting from given prefix
        candidates = []
        if start_node.is_word:
            candidates.append(prefix)
        for child in start_node.get_children():
            candidates.extend(self.__get_candidates(child, [prefix]))
        return candidates






if __name__ == "__main__":
    t = Trie()
    t.insert('car')
    t.insert('card')
    t.insert('cards')
    t.insert('cot')
    t.insert('cots')
    t.insert('trie')
    t.insert('tried')
    t.insert('tries')
    t.insert('try')
    print(t.has_substring('ca'))
    print("Total Nodes:", len(t))
    print(t)

    # explort Trie
    print(t.root)
    print(t.root.get_child('t').data)
    print(t.root.get_child('c').children)
    
    # test find() and get_cadidates()
    print('cards' in t)
    print('c' in t)
    print(t.auto_complete())
    print(t.auto_complete('c'))
    print(t.auto_complete('tri'))
    print('='*50)
    
    # test remove()
    t = Trie()
    t.insert("tre")
    t.insert("trees")
    t.insert("treed")
    t.remove("trees")
    t.remove("tre")
    print(t)
    print("Total Nodes:", len(t))
    print(t.auto_complete("t"))

    # sanity checks
    t = Trie()
    t.insert('a')
    t.insert('A')
    t.remove('AA')
    print(t)
