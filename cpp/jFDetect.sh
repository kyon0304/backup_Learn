# Filename: jFDetect.sh
# Created on:2012-2-23
# Usage: Process lots images in batch

#! /bin/bash
for pic in ./data/*.jpg
do
	./jfeatures $pic
done
