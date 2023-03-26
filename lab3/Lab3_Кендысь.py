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
i_n = 5


def xor_number(bin_num):
    return bin_num.bit_count() % 2


def gamma_xor(gamma1, gamma2):
    if gamma1 ^ gamma2 == 0:
        return 1
    else:
        return -1


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
            r = xor_number(s)
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

    def count_ones(self):
        return sum(self.gamma_seq)

    def r_stat(self, i):
        res = []
        r_sum = 0
        for t in range(self.n - 1):
            r_sum += gamma_xor(self.gamma_seq[t], self.gamma_seq[t + 1])

        res.append(r_sum)
        for j in range(1, i):
            r_sum -= gamma_xor(self.gamma_seq[self.n - j - 1], self.gamma_seq[self.n - j])
            res.append(r_sum)

        return res


def lfsr_output(lfsr_seq):
    for i in range(len(lfsr_seq)):
        print(f"LFSR {i + 1}:")
        seq_string = ','.join(map(str, lfsr_seq[i].seq))
        print(f"Period: {lfsr_seq[i].period}. Sequence: {seq_string}.")


def geffe_seq_output(geffe_seq):
    print(f"Gamma sequence: {','.join(map(str, geffe_seq))}.")


def geffe_stats_output(zeroes, ones, r_stat):
    print(f"Number of zeroes: {zeroes}.")
    print(f"Number of ones: {ones}.")
    print(f"r_i: {', '.join(map(str, r_stat))}.")


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

    print("\nTask 3. Geffe generator sequence.")
    one_sum = geffe.count_ones()
    geffe_stats_output(N - one_sum, one_sum, geffe.r_stat(i_n))
