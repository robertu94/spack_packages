# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.libpressio_rmetric import LibpressioRmetric as BuiltinLibPressioRmetric


class LibpressioRmetric(BuiltinLibPressioRmetric):
    """LibPressio metric that runs R code"""

    version("0.0.8", sha256="246d98c80f1011819bdac2893035d7914b40d328aae2d50b3608a178406f95d9")
    depends_on("libpressio@0.99.4:", when="@0.0.8:")
