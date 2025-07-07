
def enc(s, shift):
    if "A" <= s <= "Z":
        return chr(ord('A') + (ord(s) - ord('A') + shift) % 26)
    else:
        return s

def encrypt(s, shift):
    return "".join([enc(x, shift) for x in s])

print(encrypt("THE EAGLE IS IN PLAY; MEET AT JOE'S.", 3))
print(encrypt("WKH HDJOH LV LQ SODB; PHHW DW MRH'V.", -3))

