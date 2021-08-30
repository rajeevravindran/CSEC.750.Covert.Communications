import sys

source_lines = open(sys.argv[1], "r").readlines()
# print(source_lines)
covert_message = sys.argv[2]

binary_covert_strings = [format(ord(ascii_char), '08b') for ascii_char in covert_message]
# print(binary_covert_strings)
final_comm = [overt_text.replace("\n", "") + covert_text.replace("1", "\t").replace("0", " ") + "\n"
              for overt_text, covert_text in
              zip(source_lines, binary_covert_strings)]
output_filename = sys.argv[1] + "_out.txt"
with open(output_filename, "w") as transport_file:
    transport_file.writelines(final_comm)
    print(f"[*] '{covert_message}' embedded inside '{output_filename}' !")
