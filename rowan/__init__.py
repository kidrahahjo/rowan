# Copyright (c) 2018 The Regents of the University of Michigan
# All rights reserved.
# This software is licensed under the BSD 3-Clause License.
R"""
The core :py:mod:`rowan` package contains functions for operating on
quaternions. The core package is focused on robust implementations of key
functions like multiplication, exponentiation, norms, and others. Simple
functionality such as addition is inherited directly from numpy due to
the representation of quaternions as numpy arrays. Many core numpy functions
implemented for normal arrays are reimplemented to work on quaternions (
such as :py:func:`allclose` and :py:func:`isfinite`). Additionally, `numpy
broadcasting
<https://docs.scipy.org/doc/numpy-1.14.0/user/basics.broadcasting.html#>`_
is enabled throughout rowan unless otherwise specified. This means that
any function of 2 (or more) quaternions can take arrays of shapes that do
not match and return results according to numpy's broadcasting rules.
"""

from __future__ import division, print_function, absolute_import

from . import calculus
from . import geometry
from . import interpolate
from . import mapping
from . import random

from .functions import (allclose, conjugate, divide, exp, expb, exp10, equal,
                        from_axis_angle, from_euler, from_matrix,
                        from_mirror_plane, inverse, isclose, isinf, isfinite,
                        isnan, is_unit, log, logb, log10, multiply, norm,
                        normalize, not_equal, power, reflect, rotate,
                        to_axis_angle, to_euler, to_matrix,
                        vector_vector_rotation)

# Get the version
import os

__version__ = 0.6.0

__all__ = ['calculus', 'geometry', 'interpolate', 'mapping', 'random',
           'allclose', 'conjugate', 'divide', 'exp', 'expb', 'exp10', 'equal',
           'from_axis_angle', 'from_euler', 'from_matrix', 'from_mirror_plane',
           'inverse', 'isclose', 'isinf', 'isfinite', 'isnan', 'is_unit', 'log',
           'logb', 'log10', 'multiply', 'norm', 'normalize', 'not_equal',
           'power', 'reflect', 'rotate', 'to_axis_angle', 'to_euler',
           'to_matrix', 'vector_vector_rotation']
