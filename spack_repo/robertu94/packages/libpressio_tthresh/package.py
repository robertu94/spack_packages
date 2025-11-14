# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
try:
    from spack_repo.builtin.packages.libpressio_tthresh.package  import LibpressioTthresh as BuiltinLibPressioTthresh
except ImportError:
    from spack_repo.builtin.packages.libpressio_tthresh.package import LibpressioTthresh as BuiltinLibPressioTthresh


class LibpressioTthresh(BuiltinLibPressioTthresh):
    """A tthresh implementation for libpressio"""
    version("0.0.10", sha256="5f9cc995c2e6086cde9cd21e2eedec032be43cc588fec5e4c14b1dd8f02d7272")
    version("0.0.9", sha256="91fd5b6d8a8711b32743992866fdabd549a07423977776a77d465020b5786f1d")
    depends_on("libpressio@1.0.0:1.0.4", when="@0.0.9")
    depends_on("libpressio@1.0.5:", when="@0.0.10:")
    depends_on("c", type="build")
