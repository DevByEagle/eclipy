cmake_minimum_required(VERSION 3.15)
project(eclipy VERSION 1.0.0)

file(GLOB SOURCES "src/*.cpp")

# Directory for easier includes
list(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake)

# Registers build options that are exposed to cmake
include(CMakeOptions.txt)

# Include CMake Modules

# Find Packages
find_package(Python COMPONENTS Interpreter Development REQUIRED)

# Include Directories
include_directories(${PROJECT_NAME} PRIVATE ${Python_INCLUDE_DIRS})

add_library(${PROJECT_NAME} MODULE ${SOURCES})

set_target_properties(${PROJECT_NAME} PROPERTIES 
  PREFIX ""
  SUFFIX "${Python3_EXTENSION_SUFFIX}"  # Use the Python extension suffix
)

# Link libraries
target_link_libraries(${PROJECT_NAME} ${Python_LIBRARIES})
