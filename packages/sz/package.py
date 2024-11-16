# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.sz import Sz as SzBuiltin, CMakeBuilder as SZCMakeBuilder


class Sz(SzBuiltin):
    version('2.1.13', commit="f4667759ead6a902110e80ff838ccdfddbc8dcd7")


class CMakeBuilder(SZCMakeBuilder):
    def cmake_args(self):
        args = super().cmake_args()
        return args
