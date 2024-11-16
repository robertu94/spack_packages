# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.libpressio_sperr import LibpressioSperr as BuiltinLibPressioSperr


class LibpressioSperr(BuiltinLibPressioSperr):
    """A LibPressio plugin for Sperr"""
    version("0.0.6", sha256="12899ca698fb7ecf72ceececbe101440f78bd7faecce72b81c08dd0012b70a0c")

    depends_on("libpressio@1.0.0:", when="@0.0.6:")
