cd .\docs

Remove-Item .\source\* -Include *.rst -Exclude index.rst

sphinx-apidoc -f -o source/ ../

.\make.bat html

cd ..