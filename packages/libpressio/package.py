# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.libpressio import Libpressio as BuiltinLibPressio


class Libpressio(BuiltinLibPressio):
    """A generic abstraction for the compression of dense tensors"""

    version("0.96.1", sha256="2305d04b57c1b49ecd5a4bda117f1252a57529c98e6bd260bfe5166a4f4d4043")
    version("0.96.0", sha256="42f563b70c4f77abffb430284f0c5bc9adba2666412ee4072d6f97da88f0c1a0")

    variant("szx", default=False, description="build support for SZx", when="@0.87.0:")
    depends_on("szx", when="+szx")
    depends_on("libstdcompat@0.0.16:", when="@0.93.0:")

    def cmake_args(self):
        args = super().cmake_args()
        if "+szx" in self.spec:
            args.append("-DLIBPRESSIO_HAS_SZx=ON")
        return args
