from spack import *


class Azureiot(CMakePackage):
    """The Microsoft Azure IOT SDK for C"""

    homepage = "https://azure.microsoft.com/en-us/overview/iot"
    url      = "https://github.com/Azure/azure-iot-sdk-c/archive/2020-01-22.tar.gz"
    git      = "https://github.com/Azure/azure-iot-sdk-c/"

    version('2020-01-22', tag="2020-01-22", submodules=True)

    depends_on('curl@7.56:')
    depends_on('openssl')
    depends_on('libuuid')
    depends_on('cmake@3.0:', type=("build",))

    variant("prov_client", description="build the provisioning client", default=True)
    variant("edge_modules", description="build the edge modules", default=True)
    variant("hsm", description="which hsm modules to build", 
            values=("sastoken", "symm_key", "x509"), multi=True,
            default="sastoken,symm_key,x509"
            )
    variant("python", description="build the python modules", default=False)
    extends("python", when="+python")

    def cmake_args(self):
        args = []
        if "+prov_client" in self.spec:
            args.append("-Duse_prov_client=ON")
        if "+edge_module" in self.spec:
            args.append("-Duse_prov_client=ON")
        if "hsm=sastoken" in self.spec:
            args.append("-Dhsm_type_sastoken=ON")
        if "hsm=x509" in self.spec:
            args.append("-Dhsm_type_x509=ON")
        if "hsm=symm_key" in self.spec:
            args.append("-Dhsm_type_symm_key=ON")
        return args
