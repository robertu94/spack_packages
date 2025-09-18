# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
try:
    from spack_repo.builtin.packages.libpressio_opt.package  import LibpressioOpt as BuiltinLibpressioOpt
except ImportError:
    from spack_repo.builtin.packages.libpressio_opt.package import LibpressioOpt as BuiltinLibpressioOpt


class LibpressioOpt(BuiltinLibpressioOpt):
    """Metacompressor which preforms optimization of compressor settings for LibPressio"""

