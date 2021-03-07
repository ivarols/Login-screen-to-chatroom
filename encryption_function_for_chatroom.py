import math

accessable_digits = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'a': 10, 'b': 11, 'c': 12, 'd': 13,
    'e': 14, 'f': 15, 'g': 16, 'h': 17,
    'i': 18, 'j': 19, 'k': 20, 'l': 21,
    'm': 22, 'n': 23, 'o': 24, 'p': 25,
    'q': 26, 'r': 27, 's': 28, 't': 29,
    'u': 30, 'v': 31, 'w': 32, 'x': 33,
    'y': 34, 'z': 35, 'A': 36, 'B': 37,
    'C': 38, 'D': 39,
    'E': 40, 'F': 41, 'G': 42, 'H': 43,
    'I': 44, 'J': 45, 'K': 46, 'L': 47,
    'M': 48, 'N': 49, 'O': 50, 'P': 51,
    'Q': 52, 'R': 53, 'S': 54, 'T': 55,
    'U': 56, 'V': 57, 'W': 58, 'X': 59,
    'Y': 60, 'Z': 61, '.': 62, ',': 63,
    '!': 64, '?': 65, '"': 66, '#': 67,
    '€': 68, '%': 69, '&': 70, '@': 71,
    '/': 72, '(': 73, ')': 74, '=': 75,
    '-': 76, '_': 77, 'å': 78, 'ä': 79,
    'ö': 80, 'Å': 81, 'Ä': 82, 'Ö': 83,
    ':': 84, ';': 85

}
accessable_digits2 = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 'a', '11': 'b', '12': 'c', '13': 'd',
    '14': 'e', '15': 'f', '16': 'g', '17': 'h',
    '18': 'i', '19': 'j', '20': 'k', '21': 'l',
    '22': 'm', '23': 'n', '24': 'o', '25': 'p',
    '26': 'q', '27': 'r', '28': 's', '29': 't',
    '30': 'u', '31': 'v', '32': 'w', '33': 'x',
    '34': 'y', '35': 'z', '36': 'A', '37': 'B', '38': 'C', '39': 'D',
    '40': 'E', '41': 'F', '42': 'G', '43': 'H',
    '44': 'I', '45': 'J', '46': 'K', '47': 'L',
    '48': 'M', '49': 'N', '50': 'O', '51': 'P',
    '52': 'Q', '53': 'R', '54': 'S', '55': 'T',
    '56': 'U', '57': 'V', '58': 'W', '59': 'X',
    '60': 'Y', '61': 'Z', '62': '.', '63': ',',
    '64': '!', '65': '?', '66': '"', '67': '#',
    '68': '€', '69': '%', '70': '&', '71': '@',
    '72': '/', '73': '(', '74': ')', '75': '=',
    '76': '-', '77': '_', '78': 'å', '79': 'ä',
    '80': 'ö', '81': 'Å', '82': 'Ä', '83': 'Ö',
    '84': ':', '85': ';'
}


# ---------------------------------------------
# This function validates the input message to make sure it can be encrypted
# ---------------------------------------------
def password_validator(password_dcm_mv, password_input_base_mv):
    word_list_message_mv = password_dcm_mv.split()
    i = 0
    for j in range(0, len(word_list_message_mv)):
        while i < len(word_list_message_mv[j]):
            word = word_list_message_mv[j]
            if len(word_list_message_mv) == 1 and len(word) == 1:
                return 1
            elif accessable_digits.get(str(word[i])) is None:
                return 2
            elif accessable_digits.get(str(word[i])) >= int(password_input_base_mv):
                return 2

            i += 1
        i = 0
        j += 1
    return 3


# ---------------------------------------------
# This function encrypts the message
# ---------------------------------------------
def password_encryption(message_mdc_mec):
    message_word_list_mec = message_mdc_mec.split()
    message_base10_mec = 0
    encrypted_message_mec = ""
    key_content_mec = ""
    message_input_base_mec = int(accessable_digits2.__len__())
    # Goes through the following procedure for each word in the message
    for h in range(0, len(message_word_list_mec)):

        # convert message in to Base-10
        for i in range(0, len(message_word_list_mec[h])):
            message_base10_mec += int(accessable_digits.get(str(message_word_list_mec[h][i]))) * (
                    int(message_input_base_mec) ** (len(message_word_list_mec[h]) - 1 - i))
            i += 1

        # Finds base for encryption each word - equation
        encrytion_base_mec = ((((((math.ceil(math.sin(len(str(message_base10_mec))))) + 50) ** len(
            str(message_base10_mec))) + message_base10_mec) ** (h + 5)) % 20) + 62
        key_content_mec += f'{encrytion_base_mec}.'

        # finding the highest power in output-base
        j = 0

        while int(message_base10_mec) > (int(encrytion_base_mec) ** j):
            j += 1

        # converts from base-10 to output-base
        k = 1

        for exp in range(1, j + 1):
            while int(message_base10_mec) >= (k * (int(encrytion_base_mec) ** (j - exp))):
                k += 1
            k -= 1
            encrypted_message_mec += str(accessable_digits2.get(str(k)))
            message_base10_mec = int(message_base10_mec) - (int(k) * (int(encrytion_base_mec) ** (j - exp)))
            k = 1
            exp += 1
        encrypted_message_mec += "§"


    return encrypted_message_mec, key_encrypter(key_content_mec)


# --------------------------------------------
# This function decrypts the encrypted message
# --------------------------------------------
def message_decryption(encrypted_password_dmc, key_content_mdc):
    # list encrypted word

    encrypted_message_list = list()
    encrypted_message_word = ""
    j = 0
    for i in range(1, len(encrypted_password_dmc)):
        if encrypted_password_dmc[i] == "§":
            for k in range(j, i):
                encrypted_message_word += encrypted_password_dmc[k]
            j = i + 1
            encrypted_message_list.append(encrypted_message_word)
            encrypted_message_word = ""
        i += 1
    # list keys -> all bases used to encrypted every word in the message
    key_list = list()
    keys = ""
    b = 0
    for a in range(1, len(key_content_mdc)):
        if key_content_mdc[a] == ".":
            for c in range(b, a):
                keys += key_content_mdc[c]
            b = a + 1
            key_list.append(keys)
            keys = ""
        a += 1

    # convert encrypted words to base 10
    decryption_base10_list = list()
    decryption_base10 = 0
    for input1 in range(0, len(encrypted_message_list)):
        word = encrypted_message_list[input1]
        base_dec = key_list[input1]
        for i in range(0, len(word)):
            decryption_base10 += int(
                int(accessable_digits.get(str(word[i]))) * (int(base_dec) ** int(int(len(word)) - 1 - i)))
            i += 1
        decryption_base10_list.append(decryption_base10)
        decryption_base10 = 0

    # covert from base 10 to base 62
    decrypted_word = ""
    decrypted_message = list()
    v = 1
    j = 1
    for input2 in range(0, len(decryption_base10_list)):
        base10number = decryption_base10_list[input2]
        int(base10number)
        basedec = accessable_digits2.__len__()

        while int(base10number) > (basedec ** j):
            j += 1

        for exp in range(1, j + 1):
            while int(base10number) >= (v * (basedec ** (j - exp))):
                v += 1
            v -= 1
            decrypted_word += (str(accessable_digits2.get(str(v))))
            base10number = int(base10number) - (int(v) * (basedec ** (j - exp)))
            exp += 1
            v = 1
        j = 0
        decrypted_message.append(decrypted_word)
        decrypted_word = ""
    decrypted_message_rb = ""
    for q in range(0, len(decrypted_message)):
        decrypted_message_rb += f'{decrypted_message[q]} '
    return decrypted_message_rb

    # --------------------------------------------
    # This function encrypts the key needed to decrypt message
    # --------------------------------------------


def key_encrypter(key_unencrypted):

    base_decrypted_keys = 63
    key_encrypted = ""
    keystr_base10 = 0

    # converts key into base-10
    for i in range(0, len(key_unencrypted)):
        keystr_base10 += int(accessable_digits.get(str(key_unencrypted[i]))) * (
                int(base_decrypted_keys) ** (len(key_unencrypted) - 1 - i))
        i += i
    keystr_base10 = keystr_base10 ** 5


    # Base for encryption key
    key_encryption_base = int(accessable_digits2.__len__())

    # finding the highest power in output-base
    j = 0

    while int(keystr_base10) > (int(key_encryption_base) ** j):
        j += 1

    # converts from base-10 to output-base
    k = 1
    for exp in range(1, j + 1):
        while int(keystr_base10) >= (k * (int(key_encryption_base) ** (j - exp))):
            k += 1
        k -= 1
        key_encrypted += str(accessable_digits2.get(str(k)))
        keystr_base10 = int(keystr_base10) - (int(k) * (int(key_encryption_base) ** (j - exp)))

        k = 1
        exp += 1

    return key_encrypted

    # --------------------------------------------
    # This function decrypts the key
    # --------------------------------------------


def key_decrypter(encrypted_key):
    base_decrypted_keys = accessable_digits2.__len__()
    key_decrypted = ""
    keystr_base10 = 0
    # converts key into base-10
    for i in range(0, len(encrypted_key)):
        keystr_base10 += int(accessable_digits.get(str(encrypted_key[i]))) * (
                int(base_decrypted_keys) ** (len(encrypted_key) - 1 - i))
        i += 1
    keystr_base10 = int(keystr_base10) ** (1/5)
    # Base for encryption key
    key_encryption_base = 63

    # finding the highest power in output-base
    j = 0

    while int(keystr_base10) > (int(key_encryption_base) ** j):
        j += 1

    # converts from base-10 to output-base
    k = 1
    for exp in range(1, j + 1):
        while int(keystr_base10) >= (k * (int(key_encryption_base) ** (j - exp))):
            k += 1
        k -= 1
        key_decrypted += str(accessable_digits2.get(str(k)))
        keystr_base10 = int(keystr_base10) - (int(k) * (int(key_encryption_base) ** (j - exp)))

        k = 1
        exp += 1

    return key_decrypted

