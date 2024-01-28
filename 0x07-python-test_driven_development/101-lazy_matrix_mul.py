#!/usr/bin/python3
"""
This module can multiply 2 matricies using numpy module
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    multiply the 2 matrix that is given
    Args:
        m_a: input the first matrix
        m_b: input THE second matrix
    Returns:
        return m_a * m_b
    """
    return numpy.matmul(m_a, m_b)
