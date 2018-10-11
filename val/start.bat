@echo off
"%JAVA_HOME%\bin\java" -Dfile.encoding=utf-8 -Djava.file.encoding=UTF-8 -jar -Xms1024m -Xmx1024m C:\val\val.jar --basedir C:\val --filetype shp --cidx 2 --layerdefpath C:\val\수치지도20layer.json --valoptpath C:\val\수치지도20option.json --objfilepath C:\val\digitalmap20.zip --crs EPSG:5186

pause>nul