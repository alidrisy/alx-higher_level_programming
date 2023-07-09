#!/usr/bin/python3
"""Define matrix_mul function"""


def matrix_mul(m_a, m_b):
    """multiplies 2 matrices"""

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
        if m_a == [[]] or i == []:
            raise ValueError("m_a can't be empty")
        if not all(type(o) in (int, float) for o in i):
            raise TypeError("m_a should contain only integers or floats")
        if len(m_a[0]) != len(i):
            raise TypeError("each row of m_a must be of the same size")

    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")
        if m_b == [[]] or i == []:
            raise ValueError("m_b can't be empty")
        if not all(type(o) in (int, float) for o in i):
            raise TypeError("m_b should contain only integers or floats")
        if len(m_b[0]) != len(i):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    mat = []
    for i in range(len(m_a)):
        new = []
        for j in range(len(m_b[0])):
            x = 0
            for r in range(len(m_a[0])):
                x += m_a[i][r] * m_b[r][j]
            new.append(x)
        mat.append(new)
    return (mat)
