# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
try:
    from spack_repo.builtin.packages.libdistributed.package  import Libdistributed as LibdistributedBuiltin
except ImportError:
    from spack.pkg.builtin.libdistributed import Libdistributed as LibdistributedBuiltin


class Libdistributed(LibdistributedBuiltin):
    """Pre-release: a collection of facilities for MPI that create for higher level
    facilities for programming in C++"""

