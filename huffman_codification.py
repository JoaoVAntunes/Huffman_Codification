import heapq
import generate_code

def encoder(text):

    caracter_list = list(text)
    print(caracter_list)

        #1. create the frequency table, i'll be using a dictionary 
    freq_table = {}
    for char in caracter_list:
        freq_table[char] = freq_table.get(char, 0) + 1
    print("Frequência:", freq_table)


        #2. create the tree, i'll be using the heapq library
    heap = [[freq, char] for char, freq in freq_table.items()]
    heapq.heapify(heap) #organizing the elements in crescent frequency order

    #here it will put a left and right leaf together and update it's frequency, for all caracters
    while len(heap) > 1:
        left = heapq.heappop(heap)
        print(left)
        right = heapq.heappop(heap)
        print(right)
        new_node = [left[0] + right[0], [left, right]]
        print(new_node)
        heapq.heappush(heap, new_node)

    
        #3. generating the binary dictionary
    tree = heap[0]  # tree root
    bin_dict = generate_code(tree)

        #4. codifiyng the text
    huffman_code = ''.join(bin_dict[char] for char in text)

    return huffman_code, bin_dict

def decoder(huffman_code, bin_dict):
    exit_str = ''
    return exit_str

def compression_calculator(text, huffman_code):
    return



text = input("Type the text to be codified: ").strip()
while not text:
    text = input("Type the text to be codified: ").strip()
