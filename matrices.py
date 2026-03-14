from rich import print

import perf


@perf.measure
def matrix_mult(m1: list, m2: list) -> list:
    m_out = []

    for row_idx_m1, _ in enumerate(m2[0]):
        m_out_row = []

        for col_idx_m2, _ in enumerate(m1):
            m_out_cell = 0

            for idx, _ in enumerate(m1[0]):
                perf.expensive_op()
                m_out_cell += m1[row_idx_m1][idx] * m2[idx][col_idx_m2]

            m_out_row.append(m_out_cell)

        m_out.append(m_out_row)

    return m_out


def main():
    m1 = [
        [3, 2, 1, 4, 8],  #
        [1, 0, 2, 5, 9],  #
        [1, 0, 2, 5, 9],  #
        [1, 0, 2, 5, 9],  #
    ]
    m2 = [
        [1, 2, 4, 1],  #
        [0, 1, 3, 2],  #
        [4, 0, 2, 3],  #
        [4, 1, 1, 4],  #
        [4, 1, 2, 5],  #
        [4, 1, 3, 6],  #
    ]

    print(matrix_mult(m1, m2))


main()
