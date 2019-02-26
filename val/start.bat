@echo off
"%JAVA_HOME%\bin\java" -Dfile.encoding=UTF-8 -Djava.file.encoding=UTF-8 -jar -Xms256m -Xmx2048m C:\val\val.jar --basedir=C:\val --filetype=shp --cidx=2 --layerdefpath=C:\val\digitalmap20_layer.json --valoptpath=C:\val\digitalmap20_option.json --objfilepath=C:\val\digitalmap20.zip --crs=EPSG:5186

EXIT
pause>nul