# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
try:
    from spack_repo.builtin.packages.sz3.package  import Sz3 as Sz3Builtin
except ImportError:
    from spack_repo.builtin.packages.sz3.package import Sz3 as Sz3Builtin


class Sz3(Sz3Builtin):
    """SZ3 is the next generation of the SZ compressor framework"""
    conflicts("+mdz", when="@3.3.0", msg="mdz doesn't build on 3.3.0")
    version("3.3.0", commit="5d2fd2638bc3512c0b4aed594d6e8a130d0d3ed2")
    version("3.2.1", commit="61816ba1276a83b4f9aa3ee0f8299eb7b0b3528a")
