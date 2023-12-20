# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *
import shutil


class Fzvis(Package):
    """visualization software for building and understanding the effects of compression"""

    homepage = "https://szcompressor.org/next.szcompressor.github.io/"
    url = "https://github.com/YuxiaoLi1234/fzvis/archive/refs/tags/v0.1.0.tar.gz"

    maintainers("robertu94", "YuxiaoLi1234")

    license("MIT")

    version("0.1.0", sha256="0a05bf2314066c5a9fd7d23ccf1b2f041df0815df25ab5c2d8a0abf570a5f902")

    depends_on("npm", type="build")
    depends_on("libpressio+python+json", type="run")
    depends_on("py-flask", type="run")
    depends_on("py-flask-cors", type="run")

    def install(self, spec, prefix):
        npm = which("npm")
        npm("install")
        npm("run", "build")
        shutil.copytree("dist", prefix.usr.libexec.fzviz.ui)
        shutil.copyfile("src/components/main.py", prefix.bin.join("fzvis"))
        shutil.rmtree("npm-cache")

