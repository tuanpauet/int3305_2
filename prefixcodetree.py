import math
def debug(s):
    #print(s)
    return

def debug_bit(s):
    for i in range (0, len(s) * 8):
        print (get_bit(s, i), end=' ')
    print()

def get_bit(text, index): #count from zero # text defined as a string
    c = text[int(index / 8)]
    shifting_steps = 7 - index % 8
    if c & (1 << shifting_steps) != 0: return 1
    else: return 0
    
#
#Trie
#
class node: #it's a trie node and a trie as well and just a freaking trie, not some prefix things ...
    # if children.length == 0 then this is a leaf
    def __init__(self):
        #do nothing for now
        self.children = {}
        self.value = None
        return
    def insert(self, word, value):
        debug ("inserting the word " + str(word) + " with the value " + value + " to a node with address " + str(hex(id(self))))
        # words defined as arrays
        if len(word) == 0: #then set it as a leaf with this value = value
            self.value = value
        else:
            if word[0] in self.children.keys():
                self.children[word[0]].insert(word[1:], value)
            else:
                self.children[word[0]] = node()
                self.children[word[0]].insert(word[1:], value)

    def info(self, word, prefixword):
        if len(word) == 0:
            if (self.value == None):
                debug("This word doesn't exist anywhere in the tree")
            else: 
                debug("This word leads to a point which has the value of " + str(self.value))
        else:
            if self.value != None:
                debug( "A shorter version of the word, '" + str(prefixword) + "' has been found with the value of " + str(self.value))
            if word[0] not in self.children.keys():
                debug("This word doesn't exist anywhere in the tree")
            else:
                self.children[word[0]].info(word[1:], prefixword + word[0])


#
# PrefixCodeTree
#
def is_leaf (n):
        if n.value != None:
            if len(n.children) > 0:
                debug("Warning: at node with address", hex(id(n)), "both children and value have been found, which probably means the prefix code tree defined is not a valid prefix tree. continue anyway.")
            return True
        return False
    
def get_child(n, c):
        if c in n.children.keys():
            return n.children[c]
        else:
            return None

class PrefixCodeTree:
    def __init__(self):
        self.root = node() #it's a trie
        
    def insert(self, word, value):
        if len(word) == 0:
            debug("Warning: a word with length 0 is requested to be added to the trie which is likely to cause an infinite loop or repeated result.")
        self.root.insert(word, value)
        
    def decode(self, text, length): # text is defined as a string
        currently_iterated_node = self.root
        current_word = ""
        decoded_text = ""
        if len(text) * 8 < length:
            debug ("Warning: the length of the text(" + str(len(text) * 8) + ") is smaller than the length specified (" + str(length) + ")")

        i = 0
        while i < len(text) * 8 and i < length:
            debug ("reading bit index = " + str(i) + " and the result is " + str(get_bit(text, i)))
            if (is_leaf(currently_iterated_node)):
                decoded_text += currently_iterated_node.value
                debug ("A word, " + current_word + " has been decoded into " + currently_iterated_node.value)
                currently_iterated_node = self.root
                current_word = ""
                i = i - 1
            else:
                currently_iterated_node = get_child(currently_iterated_node, get_bit(text, i))
                current_word += str(get_bit(text, i))
                if currently_iterated_node == None: # which means get_child can't find any key matched in the dictionary
                    debug ("A part of compressed text can't be found anywhere in the dictionary, meaning the dictionary defined is invalid. Abort this word and continue")
                    currently_iterated_node = self.root
                    current_word = ""
            i = i + 1
        if (is_leaf(currently_iterated_node)):
                decoded_text += currently_iterated_node.value
                debug ("A word, " + current_word + " has been decoded into " + currently_iterated_node.value)
        else:
            debug("There are some bits at the end of the stream that form an incomplete word. Ignoring it")
        return decoded_text

'''
codebook = {'x1': [0],'x2': [1,0,0],'x3': [1,0,1],'x4': [1,1]}

codeTree = PrefixCodeTree()

for symbol in codebook:
    codeTree.insert(codebook[symbol], symbol)

message = codeTree.decode(b'\xd2\x9f\x20', 21)
print(message)

'''
