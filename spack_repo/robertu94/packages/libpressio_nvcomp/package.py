# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
try:
    from spack_repo.builtin.packages.libpressio_nvcomp.package  import LibpressioNvcomp as BuiltinLibPressioNvcomp
except ImportError:
    from spack_repo.builtin.packages.libpressio_nvcomp.package import LibpressioNvcomp as BuiltinLibPressioNvcomp


class LibpressioNvcomp(BuiltinLibPressioNvcomp):
    """LibPressio Bindings for NVCOMP"""
    depends_on("nvcomp@2.0.2:", when="@:0.0.2")
    depends_on("c", type="build")

