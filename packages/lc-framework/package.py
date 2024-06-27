# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.lc_framework import LcFramework as BuiltinLcFramework

class LcFramework(BuiltinLcFramework):
    """a framework for automatically creating high-speed lossless and error-bounded lossy data compression and decompression algorithms."""

