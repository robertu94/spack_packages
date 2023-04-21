from spack import *


class PyM(PythonPackage):
    """A build automation tool"""

    homepage = "https://github.com/robertu94/m"
    url      = "https://github.com/robertu94/m/archive/refs/tags/2.5.2.tar.gz"
    git      = "https://github.com/robertu94/m"

    version('master', branch="master")
    version("2.6.0", sha256="a01032bdb77cc36b315f6e6f99525bd2b4740531e327d37c64d11f5552380581")
    version("2.5.2", sha256="476181d871971640727a70d952166ad6f385ee4927d718997c7eb2f2186fac35")
    version('2.1.0', sha256='c94d82eb543014851c4a048a518742ab74ce23b617697df039f640b1494bce6a')
    version('2.0.0', sha256='a888956f202ee5089994edbe961a58e6adecc286bc5bd5d8b7ae01c81d1c6500')
    version('1.0.0', sha256='7816b6598133cfcd2949b7513fb5cb3d9ee24f0a1ac8fbc8552fc59a724b9c00')


    extends('python@3.6:')
    depends_on('py-setuptools', type=('build', 'run'))
    depends_on('py-jinja2', type=('run'))
    depends_on('cmake', type='run')
    depends_on('ninja', type='run')
    depends_on('automake', type='run')
