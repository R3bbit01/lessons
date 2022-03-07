# import sys
# print(sys.argv)
# script, encoding, error = sys.argv


# def main(language_file, encoding, errors):
#     line=language_file.readline()

#     if line:
#         print(line, encoding, errors)
#         return main(language_file, encoding, errors)

# def print_line(line, encoding, errors):
#     next_lang = line.strip()
#     raw_bytes = next_lang.encode(encoding, errors=errors)
#     cooked_string = raw_bytes.decode(encoding, errors=errors)
#     print(raw_bytes,"<===>", cooked_string)

# language = open("languages.txt", encoding="utf-8")
# main(language, encoding, error)

m = b"\xe4\xb8\xad\xe6\x96\x87"
print(m)
print(m.decode("utf-8"))