# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.libpressio import Libpressio as BuiltinLibPressio


class Libpressio(BuiltinLibPressio):
    """A generic abstraction for the compression of dense tensors"""

    version("0.99.5", sha256="e5f496cbc812cb920d29401a51a5445c1a24f270b825551a86a5e214554b6baf")

    variant("cuszp", description="add support for cuszp", default=False)
    depends_on("cusz@streams", when="@0.99.6:+cusz")
    depends_on("cuszp@2", when="+cuszp")

    def cmake_args(self):
        args = super().cmake_args()
        args.append(self.define("BUILD_TESTING", self.run_tests or self.spec.satisfies("dev_path=*")))
        args.append(self.define_from_variant("LIBPRESSIO_HAS_CUSZP", "cuszp"))
        return args
