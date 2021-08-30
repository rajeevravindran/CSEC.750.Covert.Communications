import sys
filename = sys.argv[1]
source = open(filename, "r")
lines = source.readlines()

print(f"[*] Message decoded from {filename} as :")
for line in lines:
    encoded_message = line[-8:]
    encoded_message = encoded_message.replace("\t", "1").replace(" ", "0").replace("\n", "")
    try:
        print(chr(int(encoded_message, 2)), end="")
    except ValueError:
        pass
