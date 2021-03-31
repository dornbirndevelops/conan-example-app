from conans import ConanFile, CMake


class DenaAppConan(ConanFile):
    name = "dena_app"
    version = "1.0"

    description = "Example showcase on how to develop a C++ application depending on other self-made libraries with Conan Package Manager and CMake"
    url = "https://github.com/dornbirndevelops/conan-example-app"
    license = "feel free to use it"

    settings = "os", "compiler", "build_type", "arch"

    build_policy = "missing"
    generators = "cmake_find_package"
    no_copy_source = True

    def build_requirements(self):
        self.build_requires("cmake/3.19.6@")

    def requirements(self):
        self.requires("dena_library/latest@dena/stable")

    def export_sources(self):
        self.copy("src/*")
        self.copy("CMakeLists.txt")

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def build(self):
        self._configure_cmake().build()

    def package(self):
        self._configure_cmake().install()

    def package_info(self):
        self.cpp_info.bindirs = ['bin']  # Directories where executables and shared libs can be found
