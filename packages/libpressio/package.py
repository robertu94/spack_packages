# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.libpressio import Libpressio as BuiltinLibPressio


class Libpressio(BuiltinLibPressio):
    """A generic abstraction for the compression of dense tensors"""
    version("0.93.0", sha256="1da5940aaf0190a810988dcd8f415b9c8db53bbbdfcb627d899921c89170d990")
    version("0.92.0", sha256="e9cab155deb07aabdca4ece2c826be905ed33f16c95f82f24eb01d181fce6109")
    version("0.91.1", sha256="35cd4b93e410a83c626c9c168d59ade3bf26a453bcbf50dfd77b6d141184b97c")
    version("0.91.0", sha256="6220988dc964c36cdffdbc5e055261ac7a0189ad80b67a962189683648209d2e")

    variant("szx", default=False, description="build support for SZx", when="@0.87.0:")
    depends_on("szx", when="+szx")
    depends_on("libstdcompat@0.0.16:", when="@0.93.0:")

    def cmake_args(self):
        args = super().cmake_args()
        if "+szx" in self.spec:
            args.append("-DLIBPRESSIO_HAS_SZx=ON")
        return args
