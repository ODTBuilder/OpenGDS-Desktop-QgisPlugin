# -*- coding: utf-8 -*-
"""
/***************************************************************************
 a
                                 A QGIS plugin
 aa
                              -------------------
        begin                : 2018-02-23
        git sha              : $Format:%H$
        copyright            : (C) 2018 by aa
        email                : aaa
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""


from qgis.core import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
from PyQt4.QtCore import *
import os.path
import os
import collections
import subprocess
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Initialize Qt resources from file resources.py
import resources

# Import the code for the DockWidget
from aa_dockwidget import aDockWidget
import os.path


class a:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface

        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)

        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'a_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&GeoDT')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'GeoDT')
        self.toolbar.setObjectName(u'GeoDT')

        #print "** INITIALIZING a"

        self.pluginIsActive = False
        self.dockwidget = None



    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('a', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action


    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/a/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'GeoDT'),
            callback=self.run,
            parent=self.iface.mainWindow())

    #--------------------------------------------------------------------------

    def onClosePlugin(self):
        """Cleanup necessary items here when plugin dockwidget is closed"""

        #print "** CLOSING a"

        # disconnects
        self.dockwidget.closingPlugin.disconnect(self.onClosePlugin)

        # remove this statement if dockwidget is to remain
        # for reuse if plugin is reopened
        # Commented next statement since it causes QGIS crashe
        # when closing the docked window:
        # self.dockwidget = None

        self.pluginIsActive = False


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""

        #print "** UNLOAD a"

        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&GeoDT'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar

    #--------------------------------------------------------------------------

    def run(self):
        """Run method that loads and starts the plugin"""
        self.ini_flag=True

        if not self.pluginIsActive:
            self.pluginIsActive = True


            if self.dockwidget == None:

                self.dockwidget = aDockWidget(self.iface)
                layers = self.iface.legendInterface().layers()
                self.dockwidget.go_btn.clicked.connect(self.do_join)
                self.dockwidget.close_btn.clicked.connect(self.do_close)
                self.dockwidget.close_btn_2.clicked.connect(self.do_close)
                self.dockwidget.load1.clicked.connect(self.do_load1)
                self.dockwidget.load2.clicked.connect(self.do_load2)
                self.dockwidget.load3.clicked.connect(self.do_load3)
                # my_dict = {u'수치지도 1.0': 1,
                #            u'수치지도 2.0': 2,
                #            u'지하시설물 1.0': 3,
                #            u'지하시설물 2.0': 4,
                #            u'임상도': 5
                #            }
                listCidx = [ u'수치지도 1.0', u'수치지도 2.0', u'지하시설물 1.0', u'지하시설물 2.0', u'임상도']
                self.dockwidget.cidx.addItems(listCidx)
                listCrs=[u'EPSG:5186',u'EPSG:5187']
                self.dockwidget.crs.addItems(listCrs)
                self.dockwidget.path1.setText(u'C:/val/임상도layer.json')
                self.dockwidget.path2.setText(u'C:/val/임상도option.json')
                self.dockwidget.path3.setText(u'C:/val/50000.zip')

                self.BasePath = 'C:/val/error/'
                self.listLayer = []  ## 추가된 레이어 리스트 목록 저장
                self.ini_setting()
                self.ini_event()
                self.ini_flag=False




            # connect to provide cleanup on closing of dockwidget
            self.dockwidget.closingPlugin.connect(self.onClosePlugin)

            # show the dockwidget
            # TODO: fix to allow choice of dock location
            self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dockwidget)
            self.dockwidget.show()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def ini_event(self):
        self.dockwidget.filelist1.currentIndexChanged.connect(self.changeCombobox1)
        self.dockwidget.filelist2.activated.connect(self.changeCombobox2)
        self.dockwidget.tableWidget.clicked.connect(self.viewClicked)

    def ini_setting(self):
        self.dockwidget.filelist1.clear()
        self.dockwidget.filelist2.clear()
        self.dockwidget.tableWidget.clear()
        fileList1 = os.listdir(self.BasePath)
        fileList1.reverse()
        self.dockwidget.filelist1.addItems(fileList1)
        self.changeCombobox1()
        self.changeCombobox2()

    def changeCombobox1(self):
        self.dockwidget.filelist2.clear()
        fileList2 = os.listdir(self.BasePath + self.dockwidget.filelist1.currentText())
        shplist=[]
        for file in fileList2:
            if file.endswith('.shp'):
                shplist.append(str(file).replace(".shp", ""))
        self.dockwidget.filelist2.addItems(shplist)

    def changeCombobox2(self):
        # if not self.filelist2.currentText():
        #     return
        for lyr in self.listLayer:
            try:
                vl = self.iface.legendInterface().layers()[self.findlayer(lyr.name())]
                QgsMapLayerRegistry.instance().removeMapLayer(vl.id())
            except:
                pass
        if self.ini_flag:
            return

        filePath = self.BasePath + self.dockwidget.filelist1.currentText()+'/'+ self.dockwidget.filelist2.currentText()+'.shp'
        layer = QgsVectorLayer(filePath, self.dockwidget.filelist2.currentText(), 'ogr')
        self.listLayer.append(layer)
        QgsMapLayerRegistry.instance().addMapLayer(layer, True)
        tableFiled=[]
        self.dockwidget.tableWidget.clear()
        for filed in layer.fields():
            # QMessageBox.warning(self.iface.mainWindow(), "File Make ", str(filed.name()))
            tableFiled.append(filed.name())
        tableFiled.append('id')
        self.dockwidget.tableWidget.setColumnCount(len(tableFiled))
        self.dockwidget.tableWidget.setRowCount(layer.featureCount())
        self.dockwidget.tableWidget.setHorizontalHeaderLabels(tableFiled)
        self.dockwidget.tableWidget.hideColumn(len(tableFiled)-1)
        feats=layer.getFeatures()
        self.activeLayer=layer
        self.hideFiled = len(tableFiled)-1

        # QMessageBox.warning(self.iface.mainWindow(), "File Make ", str(layer.featureCount()))
        i=0
        for feat in feats :
            j=0
            for filed in layer.fields():
                try:
                    m = QTableWidgetItem(feat.attribute(filed.name()))
                    self.dockwidget.tableWidget.setItem(i, j, m)
                except:
                    pass
                j = j + 1
            m = QTableWidgetItem(str(feat.id()))
            self.dockwidget.tableWidget.setItem(i, j,m)
            i = i + 1
            # QMessageBox.warning(self.iface.mainWindow(), "File Make ", str(feat.id()))


    def viewClicked(self):
        if not self.activeLayer:
            return
        com = self.hideFiled
        row = self.dockwidget.tableWidget.currentRow()
        id = self.dockwidget.tableWidget.item(row, com).text()
        self.activeLayer.setSelectedFeatures([int(id)])  # id 값 선택
        canvas = self.iface.mapCanvas()
        canvas.zoomToSelected(self.activeLayer)
        canvas.zoomScale(500)
        # canvas.zoomOut()
        self.iface.mapCanvas().refresh()




    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    def select_output_file(self):
        filename = QFileDialog.getOpenFileName(self.dockwidget, "Select output file ", "", '*.*')
        self.dlg.lineEdit.setText(filename)

    def do_load1(self):
        filename = QFileDialog.getOpenFileName(self.dockwidget, u"레이어 정의 옵션 경로", "", '*.*')
        self.dockwidget.path1.setText(filename)


    def do_load2(self):
        filename = QFileDialog.getOpenFileName(self.dockwidget, u"검수 옵션 경로", "", '*.*')
        self.dockwidget.path2.setText(filename)


    def do_load3(self):
        filename = QFileDialog.getOpenFileName(self.dockwidget, u"검수 대상 파일 경로", "", '*.*')
        self.dockwidget.path3.setText(filename)


    def do_join(self):
        if self.dockwidget.path1.text() =='' or self.dockwidget.path2.text()=='' or self.dockwidget.path3.text() =='':
            if self.dockwidget.path1.text() =='':
                QMessageBox.warning(self.iface.mainWindow(), u'알림', u'레이어 정의 옵션 경로를 입력해주세요')
                return 
            if self.dockwidget.path2.text() =='':
                QMessageBox.warning(self.iface.mainWindow(), u'알림', u'검수 옵션 경로를 입력해주세요')
                return
            if self.dockwidget.path3.text() =='':
                QMessageBox.warning(self.iface.mainWindow(), u'알림', u'검수 대장 파일 경로를 입력해주세요')
                return
                
        else:
            cidx= str(self.dockwidget.cidx.currentIndex() + 1)
            String = 'java -Dfile.encoding=utf-8 -Djava.file.encoding=UTF-8 -jar -Xms1024m -Xmx1024m C:/val/val.jar --basedir C:/val --filetype shp --cidx %s --layerdefpath %s --valoptpath %s --objfilepath %s --crs EPSG:5186' % (cidx, self.dockwidget.path1.text(),self.dockwidget.path2.text(),self.dockwidget.path3.text())

            # String = 'C:/val/val.jar  --basedir C:/val --filetype shp --cidx %s --layerdefpath %s --valoptpath %s --objfilepath %s --crs EPSG:5186' % (cidx, self.dockwidget.path1.text(),self.dockwidget.path2.text(),self.dockwidget.path3.text())
            QgsMessageLog.logMessage(u"qString --> %s" % String)

            # subprocess.call(['java', '-jar','C:/val/val.jar' ,'c:\\textMining.txt'])
            os.system('cmd.exe')
            os.system(String)
            # subprocess.Popen(String, shell=True)
            QMessageBox.warning(self.iface.mainWindow(), u'알림', String)
            # os.system(String)

        self.dockwidget.tabWidget.setCurrentIndex(1)
        self.ini_setting()








    def findlayer(self, s):
        # QMessageBox.warning(self.iface.mainWindow(), "File Make ", 'find')
        layers = self.iface.legendInterface().layers()
        i = -1
        for layer in layers:
            u = layer.name()
            i = i + 1
            if u == s:
                return i



    def do_close(self):
        self.dockwidget.close()

