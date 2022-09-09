cmake_minimum_required(VERSION 3.16.3)

project(module)

set(library_name "${PROJECT_NAME}_lib")

add_library(${library_name}
    SHARED
    src/template.c
)

# Use a generator expression so that the specified folder is used directly, without any
# configuration-dependent suffix.
#
# See https://cmake.org/cmake/help/v3.8/prop_tgt/LIBRARY_OUTPUT_DIRECTORY.html
set_target_properties(${library_name} PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/lib/$<0:>
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/lib/$<0:>
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/lib/$<0:>
)

IF(UNIX)
    target_link_libraries(${library_name} PUBLIC m)
ENDIF(UNIX)

target_include_directories(${library_name} 
    PUBLIC inc
)

find_package(Python3 COMPONENTS Interpreter REQUIRED)

add_custom_command(TARGET ${library_name} POST_BUILD
    COMMAND ${Python3_EXECUTABLE} build_script.py ${PROJECT_NAME} ${library_name}
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)
