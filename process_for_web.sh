#!bin/zsh
# xsltproc -xinclude -stringparam publisher publisher-file.xml ../mathbook/xsl/pretext-html.xsl main.ptx
pretext build web
python3 add_donate_button.py
rm ./output/web/*.html~
