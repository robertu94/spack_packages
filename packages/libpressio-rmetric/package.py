# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
try:
    from spack_repo.builtin.packages.libpressio_rmetric.package  import LibpressioRmetric as BuiltinLibPressioRmetric
except ImportError:
    from spack.pkg.builtin.libpressio_rmetric import LibpressioRmetric as BuiltinLibPressioRmetric


class LibpressioRmetric(BuiltinLibPressioRmetric):
    """LibPressio metric that runs R code"""

