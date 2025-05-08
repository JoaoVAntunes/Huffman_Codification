import heapq
from itertools import count
from generate_code import generate_codes

def encoder(text):
    # 1. Create a list of characters from the text
    char_list = list(text)
    print("Characters:", char_list)

    # 2. Create the frequency table using a dictionary
    freq_table = {}
    for char in char_list:
        freq_table[char] = freq_table.get(char, 0) + 1
    print("Frequency table:", freq_table)

    # 3. Build the Huffman tree using a min-heap (heapq)
    counter = count()  # Counter to avoid conflicts when frequencies are equal
    heap = [[freq, next(counter), char] for char, freq in freq_table.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        new_node = [left[0] + right[0], next(counter), [left, right]]
        heapq.heappush(heap, new_node)

    # 4. Generate the binary dictionary (character -> binary code)
    tree = heap[0]
    bin_dict = generate_codes(tree)
    print("Binary dictionary:", bin_dict)

    # 5. Encode the input text using the binary dictionary
    huffman_code = ''.join(bin_dict[char] for char in text)
    print("Huffman code:", huffman_code)

    return huffman_code, bin_dict

def decoder(huffman_code, bin_dict):
    # Invert the dictionary to decode (binary code -> character)
    inv_dict = {v: k for k, v in bin_dict.items()}
    print("Inverted dictionary:", inv_dict)

    current = ''
    decoded = ''
    for bit in huffman_code:
        current += bit
        if current in inv_dict:
            decoded += inv_dict[current]
            current = ''
    print("Decoded string:", decoded)
    return decoded

def compression_calculator(text, huffman_code):
    # 1 character = 8 bits (ASCII assumption)
    bits_plain_text = len(text) * 8
    bits_huffman = len(huffman_code)

    compression_rate = bits_huffman / bits_plain_text
    space_saved = (1 - compression_rate) * 100

    print(f"\nOriginal size: {bits_plain_text} bits")
    print(f"Huffman encoded size: {bits_huffman} bits")
    print(f"Compression rate: {compression_rate:.2f}")
    print(f"Space saved: {space_saved:.2f}%")

    return compression_rate, space_saved

# --- Main program ---

text = input("Type the text to be codified: ").strip()
while not text:
    text = input("Type the text to be codified: ").strip()

huff_code, bin_dict = encoder(text)
final_string = decoder(huff_code, bin_dict)
compression_calculator(text, huff_code)
