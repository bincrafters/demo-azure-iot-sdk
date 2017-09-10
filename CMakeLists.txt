project(IothubSampleClient)
cmake_minimum_required(VERSION 3.7)

include(conan_include.cmake)

add_executable(${PROJECT_NAME} 
	src/iothub_sample_client.cpp
)

target_link_libraries(${PROJECT_NAME} 
	crypt32 ws2_32 secur32 advapi32 ncrypt winhttp
	CONAN_PKG::Azure-IoT-SDK-C
	CONAN_PKG::Azure-C-Shared-Utility
)

target_include_directories(${PROJECT_NAME}
    PUBLIC 
		${PROJECT_SOURCE_DIR}/include
)
