%module ome_files
%{
#include <ome/files/in/OMETIFFReader.h>
using ome::files::detail::FormatReader;
using ome::files::dimension_size_type;
%}

%include "ome/files/in/OMETIFFReader.h"
