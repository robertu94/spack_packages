# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.libpressio_tthresh import LibpressioTthresh as BuiltinLibPressioTthresh


class LibpressioTthresh(BuiltinLibPressioTthresh):
    """A tthresh implementation for libpressio"""
    version("0.0.8", sha256="c6590a965b0ff3e97db1bab8ddb6e552ad4f8142623d02323dc9598da9052309")
    depends_on("libpressio@0.99.4:", when="@0.0.8:")
