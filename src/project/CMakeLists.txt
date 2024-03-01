
find_package(MPI REQUIRED COMPONENTS Fortran)
include_directories(${MPI_Fortran_INCLUDE_PATH})


file(GLOB_RECURSE SOURCES "*.f90")

add_executable(project ${SOURCES})

target_link_libraries(project ${MPI_Fortran_LIBRARIES})
