# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
try:
    from spack_repo.builtin.packages.lc_framework.package  import LcFramework as BuiltinLcFramework
except ImportError:
    from spack_repo.builtin.packages.lc_framework.package import LcFramework as BuiltinLcFramework

class LcFramework(BuiltinLcFramework):
    """a framework for automatically creating high-speed lossless and error-bounded lossy data compression and decompression algorithms."""

    version('1.3.0', commit="3d6bbf41274b93a26abbae09953d796d4ae6f429")
    depends_on("c", type="build")
    depends_on("libpressio@1.0.0:", when="@1.3.0:+libpressio")
    depends_on("libpressio@0.98.0:", when="@:1.2.2+libpressio")
