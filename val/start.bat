@echo off
"%JAVA_HOME%\bin\java" -Dfile.encoding=utf-8 -Djava.file.encoding=UTF-8 -jar -Xms1024m -Xmx1024m C:\Users\GIT\Desktop\val\val.jar --basedir C:\Users\GIT\Desktop\val --filetype shp --cidx 2 --layerdefpath C:\Users\GIT/Desktop/sample/digitalmap20_layer.json --valoptpath C:\Users\GIT/Desktop/sample/digitalmap20_option.json --objfilepath C:\Users\GIT/Desktop/sample/digitalmap20.zip --crs EPSG:5186

pause>nul