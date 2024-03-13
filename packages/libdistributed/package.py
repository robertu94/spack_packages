# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.libdistributed import Libdistributed as LibdistributedBuiltin


class Libdistributed(LibdistributedBuiltin):
    """Pre-release: a collection of facilities for MPI that create for higher level
    facilities for programming in C++"""

    version("0.4.3", sha256="fbfb473ab6da18880d64a36cf2134c18938a57fe958b822606927b2132783c0d")
