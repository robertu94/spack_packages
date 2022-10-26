# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.zfp import Zfp as BuiltinZfp


class Zfp(BuiltinZfp):

    version("1.0.0", sha256="0ea08ae3e50e3c92f8b8cf41ba5b6e2de8892bc4a4ca0c59b8945b6c2ab617c4")

    variant('utilities', default=True,  description='Build utilities')

    def cmake_args(self):
        args = super().cmake_args()
        args.append(self.define_from_variant('BUILD_UTILITIES', 'utilities'))
