#script to download wiktionary dump and unzip to data folder
wget -O tmp/enwiktionary-20191120-all-titles.gz https://ftp.acc.umu.se/mirror/wikimedia.org/dumps/enwiktionary/20191120/enwiktionary-20191120-all-titles.gz
gunzip tmp/enwiktionary-20191120-all-titles.gz
