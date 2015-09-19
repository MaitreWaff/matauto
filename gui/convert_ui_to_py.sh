#!/bin/bash
# Convertit les *.ui en *.py

#for i in `ls *.ui`; do pyuic4 -x $i -o ${i%.*}."pyw"; done
for i in `ls *.ui`
do 
	echo  "Generation de (".${i%.*}."pyw)"
	pyuic4 -x $i -o ${i%.*}."pyw"
done

#pyuic4 -x 
