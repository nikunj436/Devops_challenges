#!/usr/bin/bash
for i in inputs/*; do
    #echo $i
    o=$(echo $i | sed 's|inputs|outputs_multifile|' )  #not for global
    o=$(echo $o | sed 's|input|output|')
    #echo $o

    sed -E -e 's|([[:alnum:]]+)\s+\1|\1|g' $i > $o
done
