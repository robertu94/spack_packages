# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
try:
    from spack_repo.builtin.packages.libpressio_errorinjector.package  import LibpressioErrorinjector as BuiltinLibPressioErrorInjector
except ImportError:
    from spack_repo.builtin.packages.libpressio_errorinjector.package import LibpressioErrorinjector as BuiltinLibPressioErrorInjector


class LibpressioErrorinjector(BuiltinLibPressioErrorInjector):
    """LibPressioErrorInjector injects errors into data for sensitivity studies"""
    version('0.10.0', commit="b80b5b4bd00f82f8c526713f678ed6ac2b1cf63f")
    depends_on("libpressio@1.0.0:", when="@0.10.0:")
    depends_on("c", type="build")

