# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.libstdcompat import Libstdcompat as BuiltinStdCompat


class Libstdcompat(BuiltinStdCompat):
    """A compatibility header for C++14, 17, and 20 for C++11"""
