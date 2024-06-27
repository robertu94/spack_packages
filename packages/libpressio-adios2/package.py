# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.libpressio_adios2 import LibpressioAdios2 as BuiltinLibPressioAdios2


class LibpressioAdios2(BuiltinLibPressioAdios2):
    """An IO plugin to read/write ADIOS2 files for LibPressio"""
