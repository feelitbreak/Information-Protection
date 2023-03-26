# Лабораторная работа №3. Вариант 8. Кендысь Алексей, 3 курс, 7 группа.

n1 = 5
a1 = 0b10100
c1 = 0b11001

n2 = 7
a2 = 0b1011000
c2 = 0b1000011

n3 = 8
a3 = 0b01000110
c3 = 0b00001101

N = 10000


def count_ones(bin_num, n):
    r = 0b0
    for i in range(n):
        r ^= bin_num >> (n - i - 1)

    return r & 0b1


class LFSR:
    n = 0
    a, b, c = 0b0, 0b0, 0b0

    def __init__(self, n, a, c):
        self.n = n
        self.a = a
        self.c = c

        self.b = a
        self.period, self.seq = self.get_period_and_sequence()

    def get_period_and_sequence(self):
        res = 0
        seq = []
        while True:
            seq.append(self.b & 0b1)

            s = self.b & self.c
            r = count_ones(s, self.n)
            self.b = (r << (self.n - 1)) | (self.b >> 1)

            res += 1
            if self.b == self.a:
                break

        return res, seq


class GeffeGenerator:
    n = 0
    gamma_seq = []
    lfsr_seq = []

    def __init__(self, n, lfsr_seq):
        self.n = n
        self.lfsr_seq = lfsr_seq

        self.gamma_seq = self.get_gamma_seq()

    def get_gamma_seq(self):
        res = []

        seq1 = self.lfsr_seq[0].seq
        seq2 = self.lfsr_seq[1].seq
        seq3 = self.lfsr_seq[2].seq

        per1 = self.lfsr_seq[0].period
        per2 = self.lfsr_seq[1].period
        per3 = self.lfsr_seq[2].period

        for t in range(self.n):
            gamma = (seq1[t % per1] & seq2[t % per2]) ^ ((seq1[t % per1] ^ 0b1) & seq3[t % per3])
            res.append(gamma)

        return res


def lfsr_output(lfsr_seq):
    for i in range(len(lfsr_seq)):
        print(f"LFSR {i + 1}:")
        seq_string = ','.join(map(str, lfsr_seq[i].seq))
        print(f"Period: {lfsr_seq[i].period}. Sequence: {seq_string}.")


def geffe_seq_output(geffe_seq):
    print(f"Gamma sequence: {','.join(map(str, geffe_seq))}.")


# main
if __name__ == "__main__":
    print("Task 1. Implementing LFSR.")
    lfsr1 = LFSR(n1, a1, c1)
    lfsr2 = LFSR(n2, a2, c2)
    lfsr3 = LFSR(n3, a3, c3)
    lfsr_list = [lfsr1, lfsr2, lfsr3]

    lfsr_output(lfsr_list)

    print("\nTask 2. Geffe generator sequence.")
    geffe = GeffeGenerator(N, lfsr_list)
    geffe_seq_output(geffe.gamma_seq)
