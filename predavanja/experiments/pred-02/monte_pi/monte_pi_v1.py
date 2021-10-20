from random import random


MAX_STEPEN = 9


def baci_puno_strelica(broj_strelica):
    strelice = []
    for _ in range(broj_strelica):
        x = random()
        y = random()
        strelice.append((x, y))

    return strelice

def is_strelica_u_jedinicnom_krugu(x, y):
    return x**2 + y**2 <= 1

def chaos_computing(broj_strelica):
    count = 0
    for x, y in baci_puno_strelica(broj_strelica):
        if is_strelica_u_jedinicnom_krugu(x, y):
            count += 1

    return count / broj_strelica * 4

def main():
    for stepen in range(MAX_STEPEN):
        broj_strelica = 10**stepen
        pi = chaos_computing(broj_strelica)

        print("%10d -> %f" % (broj_strelica, pi))

    print('')

if __name__ == "__main__":
    main()
