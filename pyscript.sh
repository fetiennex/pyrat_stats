#! /bin/bash

usage()
{
    echo "Usage: pyscript.sh <nb-de-tests>">&2
    exit 1
}
case $# in
    1) n=$1;;
    *) usage ;;
esac
fn=stats.csv
if [ -r $fn ]
then echo "### preexisting $fn ###" >&2; exit
fi
echo 'algorithm;mud;map_width;map_height;map_size;turns' > $fn
while read mud 
do
    while read width 
    do
        while read height 
        do
            while read rat 
            do
                python3 pyrat.py --rat "$rat" --mud_density "$mud" --height "$height" --width "$width" --test "$n" --pieces 1 --nodrawing
            done < scriptfiles/ratfile
        done < scriptfiles/heightfile
    done < scriptfiles/widthfile
done < scriptfiles/mudfile
