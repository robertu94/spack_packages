# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPytorchWavelets(PythonPackage):
    """2D Wavelet Transforms in Pytorch"""

    homepage = "https://github.com/fbcotter/pytorch_wavelets"
    git = "https://github.com/fbcotter/pytorch_wavelets"

    url = "https://github.com/fbcotter/pytorch_wavelets/archive/refs/tags/1.1.0.tar.gz"

    maintainers("robertu94")

    version("1.1.0", sha256="bb227ca3ddfb023af3105c5d430c8ff0e451ded0af58f7693d1321ad0215b941")

    depends_on("py-setuptools", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-torch", type=("build", "run"))
    depends_on("py-pywavelets", type=("build", "run"))
