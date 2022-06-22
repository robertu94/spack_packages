# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.builtin.sz import Sz


class Sz(Sz):
    """Error-bounded Lossy Compressor for HPC Data"""

    version('develop', branch='master', git="https://github.com/robertu94/sz")
