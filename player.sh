#!/bin/bash

for filename in $(ls $HOME/dokuwiki/fantasy/data/*.txt)
do
    id=$(head -2 $filename | tail -1 | cut -d":" -f4 | tr -d "}")
    if [ "$id" = "bio]]" ]; then
        id=$(head -2 $filename | tail -1 | cut -d":" -f3)
    fi
    head -1 $filename                         > temp
    echo "{{page>player:bio:${id}}}"         >> temp
    echo "{{page>player:team:${id}}}"        >> temp
    echo "{{page>player:season:2019:${id}}}" >> temp
    echo "{{page>player:history:${id}}}"     >> temp
    echo ""                                  >> temp
    echo "===== Links here ====="            >> temp
    echo "{{backlinks>.}}"                   >> temp
    echo ""                                  >> temp
    echo "/* fpl player id:${id}: */"        >> temp

    fn=$(basename ${filename})
    fname="./data/player/${fn}"
    cp temp $fname

done
