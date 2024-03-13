# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.libpressio_nvcomp import LibpressioNvcomp as BuiltinLibPressioNvcomp


class LibpressioNvcomp(BuiltinLibPressioNvcomp):
    """LibPressio Bindings for NVCOMP"""

    version("0.0.6", sha256="19ecc090b32ec77ddbdf6a3f1f823cf19c32bd8c08b0acb0f87c740961a1d9b4")
    depends_on("libpressio@0.99.4:", when="@0.0.6:")
