import sys

def main():
    # 1. Get shift amount
    shift = int(sys.argv[1])
    
    # 2. Read from Stdin
    raw_input = sys.stdin.read()
    
    # 3. Clean and Encrypt
    encoded_chars = []
    for char in raw_input.upper():
        if 'A' <= char <= 'Z':
            # Shift character and handle wrap-around
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encoded_chars.append(new_char)
            
    # 4. Format Output (Blocks of 5, 10 blocks per line)
    output = ""
    count = 0
    for i, c in enumerate(encoded_chars):
        output += c
        count += 1
        # Add space after 5 letters
        if count % 5 == 0 and i != len(encoded_chars) - 1:
            # If we reached 10 blocks (50 letters), add newline, else space
            if count % 50 == 0:
                output += "\n"
            else:
                output += " "
                
    print(output.strip())

if __name__ == "__main__":
    main()

