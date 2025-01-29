# Encode and Decode Strings

# Description: Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

def encode(strs: list[str]) -> str:
    encoded_str = ""
    for s in strs:
        encoded_str += str(len(s)) + "#" + s
    return encoded_str


def decode(s: str) -> list[str]:
    res, i = [], 0

    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        res.append(s[j+1 : j + 1 + length])

        i = j + length + 1
    return res

def main():
    strings = ["neet","code","love","you"]
    encoded_string = encode(strings)
    decoded_strings = decode(encoded_string)
    print(decoded_strings)

if __name__ == "__main__":
    main()