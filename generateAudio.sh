python3 audio.py $1

mv out.aiff out.temp

rm *.aiff

mv out.temp out.aiff
