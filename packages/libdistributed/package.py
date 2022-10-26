# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.libdistributed import Libdistributed as LibdistributedBuiltin


class Libdistributed(LibdistributedBuiltin):
    """Pre-release: a collection of facilities for MPI that create for higher level
    facilities for programming in C++"""

    version("0.4.1", sha256="62bbd4cbaf396cea7f33d62d5e79086a56ee1396d070ad3c4fd9720c50d242c0")
