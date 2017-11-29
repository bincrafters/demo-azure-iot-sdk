from conans import ConanFile


class AzureIotSdkDemoConan(ConanFile):
    name = "Azure-IOT-SDK-Demo-Conan"
    version = "1.0.0"
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    url = "https://github.com/bincrafters/azure-iot-sdk-demo-conan"
    license = "https://github.com/bincrafters/azure-iot-sdk-demo-conan/blob/master/LICENSE"
    requires = "Azure-IoT-SDK-C/1.1.27@bincrafters/stable", \
        "OpenSSL/1.0.2m@conan/stable"

    def configure(self):
        self.options["Azure-IoT-SDK-C"].shared = False
        self.options["Azure-C-Shared-Utility"].shared = False