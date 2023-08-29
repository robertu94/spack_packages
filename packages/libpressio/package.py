# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.libpressio import Libpressio as BuiltinLibPressio


class Libpressio(BuiltinLibPressio):
    """A generic abstraction for the compression of dense tensors"""

    version("0.96.4", sha256="7f012b01ce1a6c9f5897487089266de5b60659ed6b220eadba51d63613620404")
    version("0.96.3", sha256="e8f4af028d34df2f3c8eb61cfc2f93fadab7a2e2d072a30ee6a085fb344a3be4")
    version("0.96.2", sha256="2c904ec16900b67ab0188ea96d27fa4efca2c9efc1b214119451becaaeaa2d18")
    version("0.96.1", sha256="2305d04b57c1b49ecd5a4bda117f1252a57529c98e6bd260bfe5166a4f4d4043")
    version("0.96.0", sha256="42f563b70c4f77abffb430284f0c5bc9adba2666412ee4072d6f97da88f0c1a0")

    variant("openssl", default=False, description="build support for hashing options", when="@0.96.2:")
    variant("szx", default=False, description="build support for SZx", when="@0.87.0:")
    depends_on("szx", when="+szx")
    depends_on("libstdcompat@0.0.16:", when="@0.93.0:")
    depends_on("openssl", when="+openssl")

    def cmake_args(self):
        args = super().cmake_args()
        if "+szx" in self.spec:
            args.append("-DLIBPRESSIO_HAS_SZx=ON")
        if "+openssl" in self.spec:
            args.append("-DLIBPRESSIO_HAS_OPENSSL=ON")

        return args
