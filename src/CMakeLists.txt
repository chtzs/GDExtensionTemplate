# SPDX-License-Identifier: Unlicense

target_sources( ${PROJECT_NAME}
    PRIVATE
        register_types.h
        register_types.cpp
)

target_include_directories( ${PROJECT_NAME}
    PRIVATE
        "src"
)