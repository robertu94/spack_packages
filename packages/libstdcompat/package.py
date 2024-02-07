# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.libstdcompat import Libstdcompat as BuiltinStdCompat


class Libstdcompat(BuiltinStdCompat):
    """A compatibility header for C++14, 17, and 20 for C++11"""


    variant(
        "cpp_compat",
        values=("11", "14", "17", "20", "23", "auto"),
        default="auto",
        multi=False,
        description="version of the c++ standard to use and depend on",
    )
    def max_cxx_version(self):
        if self.spec.version >= Version("0.0.20"):
            try:
                self.compiler.cxx20_flag
                return "23"
            except Exception:
                pass
            try:
                self.compiler.cxx20_flag
                return "20"
            except Exception:
                pass
        try:
            self.compiler.cxx17_flag
            return "17"
        except Exception:
            pass
        try:
            self.compiler.cxx14_flag
            return "14"
        except Exception:
            pass
        self.compiler.cxx11_flag
        return "11"

    version("0.0.20", sha256="9fdc632eb135f57132953b512d8f9101e8eb4e6a88e6c3b838aaa9c51a2dbfd6")
    version("0.0.19", sha256="584ee52b1f82671e5d8fde786c46aa7e98d30104674c6f4b75dbae8d83b13f21")

