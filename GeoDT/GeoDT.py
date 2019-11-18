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
from _winreg import *
import unicodedata
import subprocess
import re
import os.path
import os
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
        # self.check_java_proc = QProcess(self.iface)
        self.baseDir = "C:\\val"
        self.errorDirPath = self.baseDir + '\\error\\'
        self.ini_flag = True
        self.lang_type = 'ko'

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

            # 자바버전 체크함수 실행
            self.check_java()
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
            self.dockwidget.radioButton_kor.toggled.connect(self.onToggledEngToKor)
            self.dockwidget.radioButton_eng.toggled.connect(self.onToggledKorToEng)
            self.process.readyRead.connect(self.print_log_event)
            self.process.finished.connect(self.process_finished_event)
            # 자바버전 체크하는 이벤트를 run에 직접 올림
            # self.check_java_proc.readyRead.connect(self.check_java)
            # 자바버전 체크 시 배치파일을 이제 사용하지 않으므로 주석처리
            # self.check_java_proc.start(self.baseDir + "\\check_java.bat")

    # 초깃값 셋팅
    def ini_setting(self):

        if self.ini_flag:
            self.dockwidget.tabWidget.setCurrentIndex(0)
            self.dockwidget.cidx.addItems([u'오픈디지털맵',u'수치지도 1.0', u'수치지도 2.0', u'지하시설물 1.0', u'지하시설물 2.0', u'임상도'])
            self.dockwidget.cidx.setCurrentIndex(1)  # 수치지도 2.0 기본
            self.dockwidget.filetype.addItems([u'shp', u'ngi'])
            self.dockwidget.crs.addItems([u'EPSG:4326', u'EPSG:3857', u'EPSG:5179', u'EPSG:5186', u'EPSG:5187'])
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

    def onToggledKorToEng(self, _checked):
        self.lang_type = 'en'
        self.dockwidget.cidx.clear()
        self.dockwidget.tabWidget.setTabText(0, u'Preferences')
        self.dockwidget.tabWidget.setTabText(1, u'Navigator')
        self.dockwidget.groupBox.setTitle(u'Option Setting')
        self.dockwidget.groupBox_2.setTitle(u'Validation Type')
        self.dockwidget.groupBox_9.setTitle(u'File Type')
        self.dockwidget.groupBox_7.setTitle(u'Layer Definition Option Path(Path)')
        self.dockwidget.groupBox_6.setTitle(u'Validation Option Path(Path)')
        self.dockwidget.groupBox_5.setTitle(u'Validation Target File Path')
        self.dockwidget.groupBox_3.setTitle(u'Coordinate System')
        self.dockwidget.go_btn.setText(u'Run')
        self.dockwidget.close_btn.setText(u'Close')
        self.dockwidget.groupBox_8.setTitle(u'Validation Work')
        self.dockwidget.groupBox_10.setTitle(u'Log')
        self.dockwidget.logLabel.setText(u'Status : Pending')
        self.dockwidget.log_detail_btn.setText(u'Detail')
        self.dockwidget.groupBox_4.setTitle(u'Verification Result')
        self.dockwidget.label.setText(u'Parent Folder')
        self.dockwidget.label_2.setText(u'Error Layer')
        self.dockwidget.close_btn_2.setText(u'Close')
        self.dockwidget.load1.setText(u'File')
        self.dockwidget.load2.setText(u'File')
        self.dockwidget.load3.setText(u'File')

        self.dockwidget.cidx.addItems(
            [u'Open Digital Map', u'Digital Map Exact position', u'Digital Map Structure', u'Underground Facilities Exact position',
             u'Underground Facilities Structure', u'Forest type Map'])
        self.dockwidget.cidx.setCurrentIndex(1)

    def onToggledEngToKor(self, _checked):
        self.lang_type = 'ko'
        self.dockwidget.cidx.clear()
        self.dockwidget.tabWidget.setTabText(0, u'환경설정')
        self.dockwidget.tabWidget.setTabText(1, u'네비게이터')
        self.dockwidget.groupBox.setTitle(u'옵션 설정')
        self.dockwidget.groupBox_2.setTitle(u'검수 종류')
        self.dockwidget.groupBox_9.setTitle(u'파일 형식')
        self.dockwidget.groupBox_7.setTitle(u'레이어 정의 옵션 경로')
        self.dockwidget.groupBox_6.setTitle(u'검수 옵션 경로')
        self.dockwidget.groupBox_5.setTitle(u'검수 대상 파일 경로')
        self.dockwidget.groupBox_3.setTitle(u'좌표계')
        self.dockwidget.go_btn.setText(u'실행')
        self.dockwidget.close_btn.setText(u'닫기')
        self.dockwidget.groupBox_8.setTitle(u'검수 작업')
        self.dockwidget.groupBox_10.setTitle(u'로그')
        self.dockwidget.logLabel.setText(u'상태 : 대기 중')
        self.dockwidget.log_detail_btn.setText(u'자세히')
        self.dockwidget.groupBox_4.setTitle(u'검수 결과')
        self.dockwidget.label.setText(u'상위 폴더')
        self.dockwidget.label_2.setText(u'SHP 파일')
        self.dockwidget.close_btn_2.setText(u'닫기')
        self.dockwidget.load1.setText(u'불러오기')
        self.dockwidget.load2.setText(u'불러오기')
        self.dockwidget.load3.setText(u'불러오기')

        self.dockwidget.cidx.addItems([u'오픈디지털맵', u'수치지도 1.0', u'수치지도 2.0', u'지하시설물 1.0', u'지하시설물 2.0', u'임상도'])
        self.dockwidget.cidx.setCurrentIndex(1)

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
        filename = QFileDialog.getExistingDirectory(self.dockwidget, u"검수 대상 파일 경로", self.baseDir)
        self.dockwidget.path3.setText(filename)

    # 파일 형식 변경 이벤트
    def change_filetype(self):
        filetypelist = [[u'shp'], [u'dxf'] ,[u'shp', u'ngi'], [u'dxf'], [u'shp'], [u'shp']]
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
            cidx = str(self.dockwidget.cidx.currentIndex())
            langtype = None

            try:
                self.dockwidget.logLabel.setText("Verification is in progress....".decode("utf-8"))
                query = self.baseDir + "\\start.bat"
                # 배치 파일 내용 삭제
                open(query, 'w').close()
                # 배치 파일 내용 삽입
                f = open(query, 'w')
                f.write("@echo off\n" +
                        '"%JAVA_HOME%\\bin\\java" ' +
                        "-Dfile.encoding=UTF-8 -Djava.file.encoding=UTF-8 -jar -Xms256m -Xmx2048m " +
                        self.baseDir + "\\val.jar " +
                        # args
                        "--basedir=" + self.baseDir + " " +
                        "--filetype=" + self.dockwidget.filetype.currentText().encode('euc-kr') + " " +
                        "--cidx=" + cidx + " " +
                        "--layerdefpath=" + self.dockwidget.path1.text().encode('euc-kr')+ " " +
                        "--valoptpath=" + self.dockwidget.path2.text().encode('euc-kr') + " " +
                        "--objfilepath=" + self.dockwidget.path3.text().encode('euc-kr') + " " +
                        "--crs=" + self.dockwidget.crs.currentText().encode('euc-kr') + " " +
                        "--langtype=" + self.lang_type +
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
                self.dockwidget.logLabel.setText("Fail.".decode("utf-8"))
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
            self.dockwidget.logLabel.setText("Procressing....".decode("utf-8") + " ( " + startTime + " / " + finishTime + " )")
            self.dockwidget.progressBar.setValue(int(percent))
        except Exception as e:
            pass

    # 검수 종료 이벤트
    def process_finished_event(self, exit_code):
        if exit_code == 200:
            self.ini_setting()
            self.dockwidget.logLabel.setText(u"Success.")
            self.dockwidget.tabWidget.setCurrentIndex(1)
            self.dockwidget.go_btn.setEnabled(True)
        else:
            self.dockwidget.logLabel.setText(u"Fail.")
            self.dockwidget.go_btn.setEnabled(True)

    # 로그 상세 버튼 이벤트
    def log_detail_btn_event(self):
        if self.dockwidget.log_detail_btn.isChecked():
            self.dockwidget.log_detail.setVisible(True)
        else:
            self.dockwidget.log_detail.setVisible(False)

     # 자바 유효성 검사 이벤트
     # 수정 : 이석재
     # 19.02.22 - 배치파일 없이 버전체크 가능

    def check_java(self):

        roots_hives = {
            "HKEY_CLASSES_ROOT": HKEY_CLASSES_ROOT,
            "HKEY_CURRENT_USER": HKEY_CURRENT_USER,
            "HKEY_LOCAL_MACHINE": HKEY_LOCAL_MACHINE,
            "HKEY_USERS": HKEY_USERS,
            "HKEY_PERFORMANCE_DATA": HKEY_PERFORMANCE_DATA,
            "HKEY_CURRENT_CONFIG": HKEY_CURRENT_CONFIG,
            "HKEY_DYN_DATA": HKEY_DYN_DATA
        }
        '''
        레지스트리 파일들을 탐색하면서 원하는 파일의 값을 읽어오기 위한 부분
        '''
        def parse_key(key):
            key = key.upper()
            parts = key.split('\\')
            root_hive_name = parts[0]
            root_hive = roots_hives.get(root_hive_name)
            partial_key = '\\'.join(parts[1:])

            if not root_hive:
                raise Exception('root hive "{}" was not found'.format(root_hive_name))

            return partial_key, root_hive

        def get_sub_keys(key):
            partial_key, root_hive = parse_key(key)

            with ConnectRegistry(None, root_hive) as reg:
                with OpenKey(reg, partial_key) as key_object:
                    sub_keys_count, values_count, last_modified = QueryInfoKey(key_object)
                    try:
                        for i in range(sub_keys_count):
                            sub_key_name = EnumKey(key_object, i)
                            yield sub_key_name
                    except WindowsError:
                        pass

        def get_values(key, fields):
            partial_key, root_hive = parse_key(key)

            with ConnectRegistry(None, root_hive) as reg:
                with OpenKey(reg, partial_key) as key_object:
                    data = {}
                    for field in fields:
                        try:
                            value, type = QueryValueEx(key_object, field)
                            data[field] = value
                        except WindowsError:
                            pass

                    return data

        def get_value(key, field):
            values = get_values(key, [field])
            return values.get(field)

        def join(path, *paths):
            path = path.strip('/\\')
            paths = map(lambda x: x.strip('/\\'), paths)
            paths = list(paths)
            result = os.path.join(path, *paths)
            result = result.replace('/', '\\')
            return result
        # key 의 경로 아래에 JAVA_HOME 과 Path 레지스트리 파일이 있음
        key = r'HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\Session Manager'
        # key 경로를 탐색하면서 Path 와 JAVA_HOME 의 레지스트리 값을 저장, 저장되면 반복문 탈출
        for sub_key in get_sub_keys(key):
            path = join(key, sub_key)
            value = get_values(path, ['Path', 'JAVA_HOME'])
            if value:
                break
        java_home=r'"%JAVA_HOME%\bin"'

        try:
            global string_java_home
            global string_path
            # 가져온 레지스트리 값을 문자열로 변환
            string_java_home = (unicodedata.normalize('NFKD', value['JAVA_HOME']).encode('ascii', 'ignore'))
            string_path = (unicodedata.normalize('NFKD', value['Path']).encode('ascii', 'ignore'))
            #  테스트용 출력. 이 출력 결과는 QGIS 내부 파이썬 콘솔에서 확인가능함
            #  GeoDT Desktop 실행 전 파이썬 콘솔을 켜 놔야 콘솔창에 값들이 출력되는 것이 확인가능
            print(string_path)
            print(string_java_home)
        except :
            # 만일 JAVA_HOME 의 값 자체가 없으면 에러 메시지 1 띄움
            QMessageBox.warning(self.iface.mainWindow(), u'알림', u'JAVA_HOME 환경 변수가 없습니다.')
            print(string_path)
            print(string_java_home)
        if "JAVA_HOME" in string_path:
            pass
        else:
            # 만일 Path 에 %JAVA_HOME%/bin 이 추가되있지 않으면 에러 메시지 2 띄움
            QMessageBox.warning(self.iface.mainWindow(), u'알림', u'PATH '
                                                                u'환경 변수에 '+java_home+' 을 추가해주세요.')

        # subprocess 모듈을 사용해 경로를 넣고 싶으면 경로 사이에 \ 이 아니라 / 이 들어가야 인식해서
        # \ 을 / 로 다 바꿔줌
        string_java_home2=string_java_home.replace('\\','/')
        # 잘 변환됬는지 테스트 출력
        print string_java_home2+'/bin/java.exe'
        # subprocess 모듈을 사용해서 사용자가 JAVA_HOME 경로의 java.exe 버전을 체크
        # cmd 의 java -version 의 결과값과 동일함
        r1 = subprocess.check_output([string_java_home2+'/bin/java.exe', '-version'],
                                     stderr=subprocess.STDOUT)
        pattern = '\"(\d+\.\d+).*\"'
        # re 모듈을 사용해서 결과값에서 필요한 버전 부분만 따오고 이를 float로 변환
        r2 = float(re.search(pattern, r1).groups()[0])
        # 잘 변환됬는지 테스트 출력
        print(r2)
        # 현재 검수 기능이 javac 1.8 버전에서만 작동하기 때문에 버전이 1.8이 아니면
        if r2==1.8:
            pass
        else:
            # 에러 메시지3 띄움
            QMessageBox.warning(self.iface.mainWindow(), u'알림', u'javac 버전이 호환되지 않습니다.')

    # 현구 들렀다감. 팀장님 나빠요.