# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
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
#     spack install qcat
#
# You can edit this file again by typing:
#
#     spack edit qcat
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Qcat(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/szcompressor/qcat"
    url      = "https://github.com/szcompressor/qcat/archive/refs/tags/1.2.tar.gz"
    git =      "https://github.com/szcompressor/qcat"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('master', branch="master")
    version('1.2', sha256='83197c1ab902558a85ab5d33d1e25d93536d47b21eefc5060cce3f674c00492e')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def configure_args(self):
        args = []
        return args
