# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-passlib
#
# You can edit this file again by typing:
#
#     spack edit py-passlib
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyPasslib(PythonPackage):
    """comprehensive password hashing framework supporting over 30 schemes"""

    homepage = "https://passlib.readthedocs.io/"
    pypi = "passlib/passlib-1.7.4.tar.gz"

    maintainers("robertu94")

    license("BSD-3-Clause", checked_by="robertu94")

    version("1.7.4", sha256="defd50f72b65c5402ab2c573830a6978e5f202ad0d984793c8dde2c4152ebe04")

    depends_on("py-setuptools", type="build")

    def config_settings(self, spec, prefix):
        settings = {}
        return settings
