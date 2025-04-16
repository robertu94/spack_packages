# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *
from spack.pkg.builtin.libpressio_predict import LibpressioPredict as BuiltinLibpressioPredict


class LibpressioPredict(BuiltinLibpressioPredict):
    """prediction tools for libpressio"""
    version("0.0.6", sha256="b26e2d7062825a61e820ca57e9ff0b47c5eccbdf41a63ee4a618faf08f1ab66b")
    version("0.0.5", sha256="4e198558f33c904344558ad09a65e62ed629e368ecb91a4e7a46ea73725ad9bb")

    variant("opt", description="enable prediction powered optimizer", default=False)
    depends_on("libpressio-opt" ,when="+opt")
    depends_on("c" , type="build")

    with when("+khan2023"):
        depends_on("sz3@3.1.8", when="@0.0.3:0.0.4")
        depends_on("sz3@3.2.1", when="@0.0.5:")
    with when("+sian2022"):
        depends_on("sz3@3.1.8", when="@0.0.3:0.0.4")
        depends_on("sz3@3.2.1", when="@0.0.5:")

    def cmake_args(self):
        args = super().cmake_args()
        args.append(self.define_from_variant("LIBPRESSIO_PREDICT_HAS_OPT", "opt"))
        return args
