# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.libpressio_rmetric import LibpressioRmetric as BuiltinLibPressioRmetric


class LibpressioRmetric(BuiltinLibPressioRmetric):
    """LibPressio metric that runs R code"""

