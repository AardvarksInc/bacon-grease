import random
import numpy as np

seed = 314159265
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "

# Get seed from user and check that it is an integer.
running = True
while running:
    try:
        seed = int(input("seed: "))
        running = False

    except:
        print("input not interpretable as integer. Please enter a valid integer.")

encode_status = input("encode (e) or decode (d): ")


def encode(message):
    out = []
    for x in range((len(message) + 1) // 2):
        sequence = 0
        try:
            sequence = np.array(
                [ALPHABET.index(message[2 * x]), ALPHABET.index(message[2 * x + 1])]
            )
        except IndexError:
            sequence = np.array(
                [ALPHABET.index(message[2 * x]), random.randint(0, len(ALPHABET) - 1)]
            )

        embedding_matrix = np.array(
            [
                [
                    random.randint(-(len(ALPHABET) - 1), len(ALPHABET) - 1),
                    random.randint(-(len(ALPHABET) - 1), len(ALPHABET) - 1),
                ],
                [
                    random.randint(-(len(ALPHABET) - 1), len(ALPHABET) - 1),
                    random.randint(-(len(ALPHABET) - 1), len(ALPHABET) - 1),
                ],
            ]
        )
        out.append(list(np.matmul(embedding_matrix, sequence)))
    return out


def decode(message: str):
    message_ints = [int(ch) for ch in message.split(" ")]
    pairs = [
        np.array([message_ints[2 * x], message_ints[2 * x + 1]])
        for x in range((len(message_ints) + 1) // 2)
    ]
    out = []
    for pair in pairs:
        embedding_matrix = np.array(
            [
                [
                    random.randint(-(len(ALPHABET) - 1), len(ALPHABET) - 1),
                    random.randint(-(len(ALPHABET) - 1), len(ALPHABET) - 1),
                ],
                [
                    random.randint(-(len(ALPHABET) - 1), len(ALPHABET) - 1),
                    random.randint(-(len(ALPHABET) - 1), len(ALPHABET) - 1),
                ],
            ]
        )

        decoding_matrix = np.linalg.inv(embedding_matrix)
        out.append(
            [
                ALPHABET[int(np.round(i)) % len(ALPHABET)]
                for i in list(np.matmul(decoding_matrix, pair))
            ]
        )
    return out


def main():
    random.seed(seed)
    if encode_status == "e":
        message = input("message: ")
        print("".join([f"{tup[0]} {tup[1]} " for tup in encode(message)]))
    elif encode_status == "d":
        ciphertext = ""
        with open("decode_file.txt", "r") as f:
            ciphertext = f.read()

        print("".join([f"{pair[0]}{pair[1]}" for pair in decode(ciphertext)]))


if __name__ == "__main__":
    main()
