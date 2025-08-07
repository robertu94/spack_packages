# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
try:
    from spack_repo.builtin.packages.libstdcompat.package  import Libstdcompat as BuiltinStdCompat
except ImportError:
    from spack.pkg.builtin.libstdcompat import Libstdcompat as BuiltinStdCompat


class Libstdcompat(BuiltinStdCompat):
    """A compatibility header for C++14, 17, and 20 for C++11"""
     version("0.0.22", sha256="d1160c3fd66966e0f6e8fc5f43fece4c47e918347c030b4a58d6f3f6930402b7")


