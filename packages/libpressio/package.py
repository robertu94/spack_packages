# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.libpressio import Libpressio as BuiltinLibPressio


class Libpressio(BuiltinLibPressio):
    """A generic abstraction for the compression of dense tensors"""
    version("0.89.0", sha256="55dd4cf05d78ef086c77b855027ae177547f320bf2d1f43e80608dd94026a0c8")

    variant("szx", default=False, description="build support for SZx", when="@0.87.0:")
    depends_on("szx", when="+szx")

    def cmake_args(self):
        args = super().cmake_args()
        if "+szx" in self.spec:
            args.append("-DLIBPRESSIO_HAS_SZx=ON")
        return args
