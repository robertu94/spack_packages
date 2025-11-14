# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
try:
    from spack_repo.builtin.packages.libpressio_sperr.package  import LibpressioSperr as BuiltinLibPressioSperr
except ImportError:
    from spack_repo.builtin.packages.libpressio_sperr.package import LibpressioSperr as BuiltinLibPressioSperr


class LibpressioSperr(BuiltinLibPressioSperr):
    """A LibPressio plugin for Sperr"""
    version("0.0.7", sha256="2845c02cfabad2892fcbae411ac468a69925db4454cac09461a016101abc5622")
    version("0.0.6", sha256="12899ca698fb7ecf72ceececbe101440f78bd7faecce72b81c08dd0012b70a0c")

    depends_on("c", type="build")
    depends_on("libpressio@1.0.0:1.0.4", when="@0.0.6:")
    depends_on("libpressio@1.0.5:", when="@0.0.7:")
