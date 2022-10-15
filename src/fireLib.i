%include "carrays.i"

%module firelib


%{
    #include "fireLib.h"
%}
%array_class(double, doubleArray);
%include "fireLib.h"
