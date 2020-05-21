cmake_minimum_required(VERSION 3.10)

project(torchcule CXX CUDA)

add_library(torchcule_atari torchcule/frontend.cpp torchcule/backend.cu)

set(PYTHON_LIBRARIES "$ENV{STDLIB_DIR}")
set(PYTHON_INCLUDE_DIRS "$ENV{PREFIX}/include/python$ENV{PY_VER}m")

message("Python libs: ${PYTHON_LIBRARIES}")
message("Python include: ${PYTHON_INCLUDE_DIRS}")

find_package(CUDAToolkit)

target_include_directories(
    torchcule_atari PUBLIC
    "${PROJECT_SOURCE_DIR}" 
    "${PROJECT_SOURCE_DIR}/third_party/pybind11/include"
    "${PROJECT_SOURCE_DIR}/third_party/agency"
    ${PYTHON_INCLUDE_DIRS}
    ${CMAKE_CUDA_TOOLKIT_INCLUDE_DIRECTORIES})