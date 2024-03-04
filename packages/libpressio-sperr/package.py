# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.libpressio_sperr import LibpressioSperr as BuiltinLibPressioSperr


class LibpressioSperr(BuiltinLibPressioSperr):
    """A LibPressio plugin for Sperr"""

    version("0.0.5", sha256="8fda62ad923b4229b9a434d5f9197010e396e972ffb9e29c2e7783ec14fdc324")
    depends_on("libpressio@0.99.4:", when="@0.0.5:")
