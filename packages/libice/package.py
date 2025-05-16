# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
try:
        from spack_repo.builtin.packages.libice.package  import Libice as BuiltinLibice
except ImportError:
    from spack.pkg.builtin.libice import Libice as BuiltinLibice

class Libice(BuiltinLibice):
    """libICE - Inter-Client Exchange Library."""
