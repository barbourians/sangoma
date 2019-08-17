#!/bin/bash

for filename in $(ls $HOME/dokuwiki/fpl/tmp/*.txt)
do
    id=$(tail -1 $filename | cut -d":" -f2)
    head -1 $filename                         > temp
    echo "{{page>player:bio:${id}}}"         >> temp
    echo "{{page>player:team:${id}}}"        >> temp
    echo "{{page>player:season:2019:${id}}}" >> temp
    echo "{{page>player:history:${id}}}"     >> temp
    echo ""                                  >> temp
    echo "===== Links here ====="            >> temp
    echo "{{backlinks>.}}"                   >> temp
    echo ""                                  >> temp
    echo "fpl player id:${id}"               >> temp

    fn=$(basename ${filename})
    fname="$HOME/dokuwiki/fpl/FILES/player/${fn}"
    mv temp $fname

done
