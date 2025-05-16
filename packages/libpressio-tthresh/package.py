# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
try:
    from spack_repo.builtin.packages.libpressio_tthresh.package  import LibpressioTthresh as BuiltinLibPressioTthresh
except ImportError:
    from spack.pkg.builtin.libpressio_tthresh import LibpressioTthresh as BuiltinLibPressioTthresh


class LibpressioTthresh(BuiltinLibPressioTthresh):
    """A tthresh implementation for libpressio"""
    version("0.0.9", sha256="91fd5b6d8a8711b32743992866fdabd549a07423977776a77d465020b5786f1d")
    depends_on("libpressio@1.0.0:", when="@0.0.9:")
