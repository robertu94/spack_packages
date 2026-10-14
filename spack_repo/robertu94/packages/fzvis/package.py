# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import shutil
from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class Fzvis(Package):
    """Visualization software for building and understanding the effects of compression"""

    homepage = "https://szcompressor.org/next.szcompressor.github.io/"
    url = "https://github.com/YuxiaoLi1234/fzvis/archive/refs/tags/v0.5.0.tar.gz"
    git = "https://github.com/YuxiaoLi1234/fzvis"

    maintainers("robertu94", "guoxiliu", "YuxiaoLi1234")

    license("MIT")

    version("dev", branch="dev")
    version(
        "0.5.0",
        sha256="67b91fcb77463a72baa6a7354a13600755953f4ee1762d1189a0e22839f28e53",
        url="https://github.com/YuxiaoLi1234/fzvis/archive/refs/tags/v0.5.0.tar.gz",
        preferred=True,
    )
    version(
        "0.4.0",
        sha256="b611db3bc277ae4f4cd3dcd7cdb09c6571c8ddf7b63ba38cd7c0fcc6476c1c35",
        url="https://github.com/YuxiaoLi1234/fzvis/archive/refs/tags/v0.4.0.tar.gz",
    )
    version(
        "0.3.0",
        sha256="2e564d03d92b14640f1c139198f0b6cd528ee3cd748d4fd971e75e0272aa91ef",
        url="https://github.com/YuxiaoLi1234/fzvis/archive/refs/tags/v0.3.0.tar.gz",
    )

    version(
        "0.2.4",
        sha256="bb7cb0a6b925a3104f049db17ef61ee3576e3a7ceff00b64ebbc66335e48fb44",
        url="https://github.com/YuxiaoLi1234/fzvis/archive/refs/tags/v0.2.4.tar.gz",
    )
    version(
        "0.2.3",
        sha256="dea16cbad1b54d376f7f3e70c64703946df313f9165d775659eff43f6a19b9ae",
        url="https://github.com/YuxiaoLi1234/fzvis/archive/refs/tags/v0.2.3.tar.gz",
    )
    version(
        "0.2.2",
        sha256="0d3893970ac775ea59cb8a845101f7e987037aa83dd71071df9bd0b42233c91f",
        url="https://github.com/YuxiaoLi1234/fzvis/archive/refs/tags/v0.2.2.tar.gz",
    )
    version(
        "0.2.1",
        sha256="7a42bf5d40c1e331d43a0ee1482f6104f0d5d4254e9d2d469362dcde4a7e8fc8",
        url="https://github.com/YuxiaoLi1234/fzvis/archive/refs/tags/v0.2.1.tar.gz",
    )
    version(
        "0.2.0",
        sha256="bd61d0210adcb70b6b2d189905b6585cd7cf3ea9840a59e6fdae14ea5bb3487d",
        url="https://github.com/YuxiaoLi1234/fzvis/archive/refs/tags/v0.2.0.tar.gz",
    )

    variant("msz", default=True, description="Enable MSz topological critical point extraction and correction")
    variant("ffcz", default=True, description="Enable FFCz frequency-domain error correction")

    depends_on("python@3.11:", type=("build", "run"))
    depends_on("py-pip", type=("build", "run"))
    depends_on("py-numpy@1.26.4", type=("build", "run"))
    depends_on("py-numcodecs@0.11.0", type=("build", "run"))
    depends_on("node-js@20:", type=("build", "run"))
    depends_on("npm", type=("build", "run"))
    depends_on("libpressio+python+json+sz+sz3+zfp", type=("run", "link"))

    depends_on("msz@fz+python+openmp", type=("build", "link", "run"), when="+msz")
    depends_on("ffcz", type=("build", "run"), when="+ffcz")

    # Legacy dependencies for 0.2.x
    depends_on("libpressio-tools", type=("run", "link"), when="@:0.2.4")
    depends_on("py-websockets", type="run", when="@:0.2.4")
    depends_on("py-flask", type="run", when="@:0.2.4")
    depends_on("py-flask-cors", type="run", when="@:0.2.4")

    def install(self, spec, prefix):
        npm = which("npm")
        if os.path.exists("package-lock.json"):
            npm("ci")
        else:
            npm("install")
        npm("run", "build")
        # Legacy installation for 0.2.x
        if spec.satisfies("@:0.2.4"):
            shutil.copytree("dist", prefix.usr.libexec.fzvis.ui)
            mkdirp(prefix.bin)
            shutil.copy2("src/components/main.py", prefix.bin.join("fzvis"))
        # New installation for 0.3.x and later
        else:
            app_dir = join_path(prefix.share, "fzvis")
            mkdirp(app_dir)
            shutil.copytree("dist", join_path(app_dir, "dist"))
            shutil.copytree("src", join_path(app_dir, "src"))
            if os.path.exists("requirements.txt"):
                shutil.copy2("requirements.txt", join_path(app_dir, "requirements.txt"))
                python = spec["python"].command
                python("-m", "pip", "install", "--prefix", prefix, "-r", "requirements.txt")

            mkdirp(prefix.bin)
            launcher = join_path(prefix.bin, "fzvis")
            with open(launcher, "w") as f:
                f.write(
                    f"""#!/usr/bin/env bash
set -euo pipefail
cd "{app_dir}"
exec "{spec['python'].command.path}" "{join_path(app_dir, 'src', 'server', 'main.py')}" "$@"
"""
                )
            set_executable(launcher)

        if os.path.exists(prefix.join("npm-cache")):
            shutil.rmtree(prefix.join("npm-cache"))

