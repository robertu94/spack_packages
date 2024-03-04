# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.libpressio_errorinjector import LibpressioErrorinjector as BuiltinLibPressioErrorInjector


class LibpressioErrorinjector(BuiltinLibPressioErrorInjector):
    """LibPressioErrorInjector injects errors into data for sensitivity studies"""

    version("0.9.0", commit="7042a11ca94f2027e60e5824c7c72c7e9a07f80f")
    depends_on("libpressio@0.99.4:", when="@0.9.0:")
