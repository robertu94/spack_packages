# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.sz import Sz as SzBuiltin, CMakeBuilder as SZCMakeBuilder


class Sz(SzBuiltin):
    pass


class CMakeBuilder(SZCMakeBuilder):
    def cmake_args(self):
        args = super().cmake_args()
        return args
