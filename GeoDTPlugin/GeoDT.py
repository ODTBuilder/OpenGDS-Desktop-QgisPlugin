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
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os.path
import os
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import resources
# Import the code for the DockWidget
from val_dockwidget import ValDockWidget
import os.path

class GeoDT:
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

        # print "** INITIALIZING a"

        self.pluginIsActive = False
        # 수정 : 윤현구
        # self.dockwidget = None
        self.dockwidget = ValDockWidget(self.iface)
        self.process = QProcess(self.iface)
        self.check_java_proc = QProcess(self.iface)
        self.baseDir = "C:\\val"
        self.errorDirPath = self.baseDir + '\\error\\'
        self.ini_flag = True


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

    # --------------------------------------------------------------------------

    def onClosePlugin(self):
        """Cleanup necessary items here when plugin dockwidget is closed"""

        # print "** CLOSING a"

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

        # print "** UNLOAD a"

        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&GeoDT'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar

    # 실제로 플러그인 실행할 때 추가하는 부분
    def run(self):
        """Run method that loads and starts the plugin"""

        if not self.pluginIsActive:
            self.pluginIsActive = True
            self.listLayer = []  # # 추가된 레이어 리스트 목록 저장


            self.ini_setting()
            self.ini_event()

            self.dockwidget.closingPlugin.connect(self.onClosePlugin)
            self.ini_flag = False
            # connect to provide cleanup on closing of dockwidget

            self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dockwidget)
            self.dockwidget.show()

    # 이벤트를 추가하는 부분
    def ini_event(self):
        if self.ini_flag:
            self.dockwidget.filelist1.currentIndexChanged.connect(self.navi_change_directory_event)
            self.dockwidget.filelist2.activated.connect(self.navi_change_shpfile_event)
            self.dockwidget.tableWidget.cellClicked.connect(self.viewClicked)
            self.dockwidget.go_btn.clicked.connect(self.execute_val)
            self.dockwidget.close_btn.clicked.connect(self.close_button_event)
            self.dockwidget.close_btn_2.clicked.connect(self.close_button_event)
            self.dockwidget.load1.clicked.connect(self.load_layer_def_event)
            self.dockwidget.load2.clicked.connect(self.load_val_opt_event)
            self.dockwidget.load3.clicked.connect(self.load_val_target_event)
            self.dockwidget.cidx.currentIndexChanged.connect(self.change_filetype)
            self.dockwidget.log_detail_btn.clicked.connect(self.log_detail_btn_event)
            self.process.readyRead.connect(self.print_log_event)
            self.process.finished.connect(self.process_finished_event)
            self.check_java_proc.readyRead.connect(self.check_java)
            self.check_java_proc.start(self.baseDir + "\\check_java.bat")

    # 초깃값 셋팅
    def ini_setting(self):
        if self.ini_flag:
            self.dockwidget.tabWidget.setCurrentIndex(0)
            self.dockwidget.cidx.addItems([u'수치지도 1.0', u'수치지도 2.0', u'지하시설물 1.0', u'지하시설물 2.0', u'임상도'])
            self.dockwidget.cidx.setCurrentIndex(1)  # 수치지도 2.0 기본
            self.dockwidget.filetype.addItems([u'shp', u'ngi'])
            self.dockwidget.crs.addItems([u'EPSG:5186', u'EPSG:5187'])
            self.dockwidget.log_detail.setVisible(False)
        self.dockwidget.filelist1.clear()
        self.dockwidget.filelist2.clear()
        self.dockwidget.tableWidget.clear()
        fileList1 = []
        try:
            fileList1 = os.listdir(u'%s'%self.errorDirPath)
        except Exception as e:
            pass
        fileList1.reverse()
        self.dockwidget.filelist1.addItems(fileList1)
        self.navi_change_directory_event()

    # 네비게이션 탭 > 폴더 변경 시 이벤트
    def navi_change_directory_event(self):
        self.dockwidget.filelist2.clear()
        fileList2 = []
        try:
            fileList2 = os.listdir(u'%s' % self.errorDirPath + u'%s' % self.dockwidget.filelist1.currentText() + "\\")
            if not fileList2:
                self.dockwidget.logLabel.setText(u'%s' % self.errorDirPath + u'%s' % self.dockwidget.filelist1.currentText() + " 경로에 파일이 없습니다.")
                self.dockwidget.log_detail.appendPlainText(u'%s' % self.errorDirPath + u'%s' % self.dockwidget.filelist1.currentText() + " 경로에 파일이 없습니다.")
                self.dockwidget.log_detail.appendPlainText(u"네비게이터가 비활성화됩니다.")
                return
        except Exception as e:
            pass

        shplist=[]
        for file in fileList2:
            if file.endswith('.shp'):
                shplist.append(str(file).decode("utf-8").replace(".shp", ""))
        self.dockwidget.filelist2.addItems(shplist)
        self.navi_change_shpfile_event()

    # 네비게이션 탭 > SHP 파일 변경 시 이벤트
    def navi_change_shpfile_event(self):

        # QGIS 레이어 패널에 중복된 err shp가 있으면 제거
        for qgis_layer in self.iface.legendInterface().layers():
            if qgis_layer.name() == self.dockwidget.filelist2.currentText():
                QgsMapLayerRegistry.instance().removeMapLayer(qgis_layer.id())
                break

        filePath = self.errorDirPath + self.dockwidget.filelist1.currentText()+'/'+ self.dockwidget.filelist2.currentText()+'.shp'
        layer = QgsVectorLayer(filePath, self.dockwidget.filelist2.currentText(), 'ogr')

        # 스타일 적용 : 빨간색 원
        label = QgsPalLayerSettings()
        label.readFromLayer(layer)
        label.enabled = True
        label.fieldName = 'errName'
        label.writeToLayer(layer)
        symbol = QgsSymbolV2.defaultSymbol(layer.geometryType())
        try:
            symbol.setColor(QColor(0, 0, 0, 0))
            symbol.setSize(10)
            symbol.symbolLayer(0).setOutlineColor(QColor(255, 0, 0))
            layer.rendererV2().setSymbol(symbol)
            self.listLayer.append(layer)
            QgsMapLayerRegistry.instance().addMapLayer(layer, True)
        except Exception as e:
            QgsMessageLog.logMessage(str(e), tag="Validating", level=QgsMessageLog.INFO)

        # 에러 네비게이터 추가
        tableFiled=[]
        self.dockwidget.tableWidget.clear()
        for filed in layer.fields():
            tableFiled.append(filed.name())
        tableFiled.append('id')
        self.dockwidget.tableWidget.setColumnCount(len(tableFiled))
        self.dockwidget.tableWidget.setRowCount(layer.featureCount())
        self.dockwidget.tableWidget.setHorizontalHeaderLabels(tableFiled)
        self.dockwidget.tableWidget.hideColumn(len(tableFiled)-1)
        feats=layer.getFeatures()
        self.activeLayer=layer
        self.hideFiled = len(tableFiled)-1

        # 피쳐 > 행 > 열
        i = 0
        for feat in feats:
            j = 0
            for filed in layer.fields():
                try:
                    m = QTableWidgetItem(feat.attribute(filed.name()))
                    # m.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                    self.dockwidget.tableWidget.setItem(i, j, m)
                except:
                    pass
                j += 1
            m = QTableWidgetItem(str(feat.id()))
            self.dockwidget.tableWidget.setItem(i, j,m)
            i += 1

    # 오류 객체 추적 이벤트
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

    # 레이어 정의 옵션 파일 열기 이벤트
    def load_layer_def_event(self):
        filename = QFileDialog.getOpenFileName(self.dockwidget, u"레이어 정의 옵션 경로", self.baseDir, '*.*')
        self.dockwidget.path1.setText(filename)

    # 검수 옵션 파일 열기 이벤트
    def load_val_opt_event(self):
        filename = QFileDialog.getOpenFileName(self.dockwidget, u"검수 옵션 경로", self.baseDir, '*.*')
        self.dockwidget.path2.setText(filename)

    # 검수 대상 파일 열기 이벤트
    def load_val_target_event(self):
        filename = QFileDialog.getOpenFileName(self.dockwidget, u"검수 대상 파일 경로", self.baseDir, '*.*')
        self.dockwidget.path3.setText(filename)

    # 파일 형식 변경 이벤트
    def change_filetype(self):
        filetypelist = [[u'dxf'] ,[u'shp', u'ngi'], [u'dxf'], [u'shp'], [u'shp']]
        self.dockwidget.filetype.clear()
        self.dockwidget.filetype.addItems(filetypelist[int(self.dockwidget.cidx.currentIndex())])

    # 검수 실행 이벤트
    def execute_val(self):
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
            cidx = str(self.dockwidget.cidx.currentIndex() + 1)
            try:
                self.dockwidget.logLabel.setText("검수 작업을 진행합니다.".decode("utf-8"))
                query = self.baseDir + "\\start.bat"
                # 배치 파일 내용 삭제
                open(query, 'w').close()
                # 배치 파일 내용 삽입
                f = open(query, 'w')
                f.write("@echo off\n" +
                        '"%JAVA_HOME%\\bin\\java" ' +
                        "-Dfile.encoding=utf-8 -Djava.file.encoding=UTF-8 -jar -Xms256m -Xmx2048m " +
                        self.baseDir + "\\val.jar " +
                        # args
                        "--basedir=" + self.baseDir + " " +
                        "--filetype=" + self.dockwidget.filetype.currentText().encode('utf-8') + " " +
                        "--cidx=" + cidx + " " +
                        "--layerdefpath=" + self.dockwidget.path1.text().encode('utf-8').replace("/", "\\", 2) + " " +
                        "--valoptpath=" + self.dockwidget.path2.text().encode('utf-8').replace("/", "\\", 2) + " " +
                        "--objfilepath=" + self.dockwidget.path3.text().encode('utf-8').replace("/", "\\", 2) + " " +
                        "--crs=" + self.dockwidget.crs.currentText().encode('utf-8') +
                        "\n\n" +
                        "EXIT\n" +
                        "pause>nul")
                f.close()
                self.dockwidget.log_detail.setPlainText("")
                self.dockwidget.progressBar.setValue(0)
                self.process.start(query)
                self.dockwidget.go_btn.setEnabled(False)

            except Exception as e:
                QgsMessageLog.logMessage("Error : " + str(e), tag="Validating", level=QgsMessageLog.INFO)
                self.dockwidget.logLabel.setText("검수 작업이 실패하였습니다.".decode("utf-8"))
                return

    # 닫기 버튼 이벤트
    def close_button_event(self):
        self.dockwidget.close()

    # 검수 실행 시 출력 이벤트
    def print_log_event(self):
        output = str(self.process.readAllStandardOutput()).decode("utf-8").replace("<br>", "\n")
        self.dockwidget.log_detail.appendPlainText(output)

        try:
            intValue = re.findall("\d+", output)
            percent = intValue[0]
            startTime = intValue[3] + ":" + intValue[4] + ":" + intValue[5]
            finishTime = intValue[6] + ":" + intValue[7] + ":" + intValue[8]
            self.dockwidget.logLabel.setText("진행중".decode("utf-8") + " ( " + startTime + " / " + finishTime + " )")
            self.dockwidget.progressBar.setValue(int(percent))
        except Exception as e:
            pass

    # 검수 종료 이벤트
    def process_finished_event(self, exit_code):
        if exit_code == 200:
            self.ini_setting()
            self.dockwidget.logLabel.setText(u"검수가 완료 되었습니다.")
            self.dockwidget.tabWidget.setCurrentIndex(1)
            self.dockwidget.go_btn.setEnabled(True)
        else:
            self.dockwidget.logLabel.setText(u"검수를 실패했습니다.")
            self.dockwidget.go_btn.setEnabled(True)

    # 로그 상세 버튼 이벤트
    def log_detail_btn_event(self):
        if self.dockwidget.log_detail_btn.isChecked():
            self.dockwidget.log_detail.setVisible(True)
        else:
            self.dockwidget.log_detail.setVisible(False)

    # 자바 유효성 검사 이벤트
    def check_java(self):
        output = str(self.check_java_proc.readAllStandardOutput()).decode("utf-8")
        if "not found." in output:
            QMessageBox.warning(self.iface.mainWindow(), u'알림', u'자바가 설치되어있지 않습니다.')
            return
        if "Java runtime is" in output:
            version = re.findall("\d+", output)[1]
            if int(version) < 8:
                QMessageBox.warning(self.iface.mainWindow(), u'알림', u'자바 ' + version + '버전에 호환되지 않습니다.')
                return
            pass

    # 현구 들렀다감. 팀장님 나빠요.