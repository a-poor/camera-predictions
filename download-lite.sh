if [ ! -d data ]
then
  mkdir data
fi
cd data
wget https://unsplash.com/data/lite/latest
unzip latest
rm -rf latest collections.tsv000 colors.tsv000 conversions.tsv000 keywords.tsv000 README.md TERMS.md
cd -