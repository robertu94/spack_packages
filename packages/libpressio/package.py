# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.libpressio import Libpressio as BuiltinLibPressio


class Libpressio(BuiltinLibPressio):
    """A generic abstraction for the compression of dense tensors"""

    version("0.99.4", sha256="091e4bac2cedca5fb9495a22eee7be718c2d04d899d56c65fc088936884eac0e")
    version("0.99.2", sha256="556d157097b2168fefde1fe3b5e2da06a952346357d46c55548d92c77d1da878")
    version("0.99.1", sha256="c9b19deaac4df5eaeecd938fea4c1752d86474f453880c0ba984ceee6bf15d35")
    version("0.99.0", sha256="b95916c4851a7ec952e5f29284e4f7477eaeff0e52a2e5b593481c72edf733d6")
    version("0.98.1", sha256="5246271fdf2e4ba99eeadfccd6224b75bf3af278a812ded74ec9adc11f6cabba")
    version("0.98.0", sha256="6b6507bf1489ff2cbeaf4c507d34e1015495c811730aa809e778f111213062db")
    version("0.97.3", sha256="631111253ec4cfd3138773eaf8280921e220b0d260985da762f0a0152e5b1b17")
    version("0.97.2", sha256="70d549ef457d5192c084fbf6304cb362d367786afe88d7b8db4eea263f9c7d43")
    version("0.96.6", sha256="a8d3269f0f5289d46471a5b85e5cd32e370edb8df45d04f5e707e0a1f64eccd8")
    version("0.96.5", sha256="7cca6f3f98dde2dbd1c9ff7462d09975f6a3630704bd01b6bef6163418a0521b")
    version("0.96.4", sha256="7f012b01ce1a6c9f5897487089266de5b60659ed6b220eadba51d63613620404")
    version("0.96.3", sha256="e8f4af028d34df2f3c8eb61cfc2f93fadab7a2e2d072a30ee6a085fb344a3be4")
    version("0.96.2", sha256="2c904ec16900b67ab0188ea96d27fa4efca2c9efc1b214119451becaaeaa2d18")
    version("0.96.1", sha256="2305d04b57c1b49ecd5a4bda117f1252a57529c98e6bd260bfe5166a4f4d4043")
    version("0.96.0", sha256="42f563b70c4f77abffb430284f0c5bc9adba2666412ee4072d6f97da88f0c1a0")

    variant("pybind", default=False, description="build support for pybind metrics", when="@0.96.0:")
    variant("openssl", default=False, description="build support for hashing options", when="@0.96.2:")
    variant("szx", default=False, description="build support for SZx", when="@0.87.0:")
    variant("blosc2", default=False, description="build support for blosc2", when="@0.98.0:")
    variant("matio", default=False, description="build support for matio", when="@0.99.0:")
    variant("clang", default=False, description="build migration tools", when="@0.99.0:")
    depends_on("sz3@3.1.8:", when="@0.98.1 +sz3")
    depends_on("szx@:1.1.0", when="@0.87.0:0.97.1 +szx")
    depends_on("szx@1.1.1:", when="@0.97.2: +szx")
    depends_on("libstdcompat@0.0.16:", when="@0.93.0:")
    depends_on("openssl", when="+openssl")
    depends_on("py-pybind11", when="+pybind")
    depends_on("cusz@0.6.0:", when="+cusz")
    depends_on("matio+shared@1.5.17:", when="+matio")
    depends_on("llvm@17: +clang", when="+clang")

    def cmake_args(self):
        args = super().cmake_args()
        if "+szx" in self.spec:
            args.append("-DLIBPRESSIO_HAS_SZx=ON")
        if "+openssl" in self.spec:
            args.append("-DLIBPRESSIO_HAS_OPENSSL=ON")
        if "+pybind" in self.spec:
            args.append("-DLIBPRESSIO_HAS_PYTHON_LAUNCH=ON")
        if "+blosc2" in self.spec:
            args.append("-DLIBPRESSIO_HAS_BLOSC2=ON")
        if "+matio" in self.spec:
            args.append("-DLIBPRESSIO_HAS_MATLABIO=ON")
        if "+clang" in self.spec:
            args.append("-DBUILD_MIGRATION_TOOLS=ON")

        return args
