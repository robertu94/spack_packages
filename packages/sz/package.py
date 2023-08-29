# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.sz import Sz as SzBuiltin, CMakeBuilder as SZCMakeBuilder


class Sz(SzBuiltin):
    variant("openmp", default=False, description="build the multithreaded version using openmp")


class CMakeBuilder(SZCMakeBuilder):
    def cmake_args(self):
        args = super().cmake_args()
        args.append(self.define_from_variant("BUILD_OPENMP", "openmp"))
        return args
