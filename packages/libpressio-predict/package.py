# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *
from spack.pkg.builtin.libpressio_predict import LibpressioPredict as BuiltinLibpressioPredict


class LibpressioPredict(BuiltinLibpressioPredict):
    """prediction tools for libpressio"""
    variant("opt", description="enable prediction powered optimizer", default=False)
    depends_on("libpressio-opt" ,when="+opt")

    def cmake_args(self):
        args = super().cmake_args()
        args.append(self.define_from_variant("LIBPRESSIO_PREDICT_HAS_OPT", "opt"))
        return args
