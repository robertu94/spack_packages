# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
try:
    from spack_repo.builtin.packages.cusz.package import Cusz as BuiltinCusz
except ImportError:
    from spack_repo.builtin.packages.cusz.package import Cusz as BuiltinCusz


class Cusz(BuiltinCusz):
    """A GPU accelerated error-bounded lossy compression for scientific data"""
    version('0.14.0', commit="e57fd7cd9df923164af9dd307b0b3d37dd9df137")

    depends_on("python", type=("build","link"), when="@0.14.0:")
    depends_on("swig", type=("build"), when="@0.14.0:")
    depends_on("cub", when="@0.6.0:^cuda@:10.2.89")

    def cmake_args(self):
        args = super().cmake_args()
        args.append("-DCMAKE_CUDA_FLAGS_DEBUG='-g -G'")
        return args
