# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.libpressio import Libpressio as BuiltinLibPressio


class Libpressio(BuiltinLibPressio):
    """A generic abstraction for the compression of dense tensors"""

    version("0.99.5", sha256="e5f496cbc812cb920d29401a51a5445c1a24f270b825551a86a5e214554b6baf")

    depends_on("cusz@streams", when="@0.99.6:")

    def cmake_args(self):
        args = super().cmake_args()
        return args
