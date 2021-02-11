cmake_minimum_required(VERSION 3.17)
project(aimi)

set(CMAKE_CXX_STANDARD 14)

include_directories(realtime-processing)

add_executable(aimi
        realtime-processing/osu_runner.cpp
        realtime-processing/osu_runner.h
        firmware/controllers.cpp
        firmware/controllers.h)
