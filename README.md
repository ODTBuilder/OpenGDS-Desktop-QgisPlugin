[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Korean](https://img.shields.io/badge/language-Korean-blue.svg)](#korean)


<a name="korean"></a>
OpenGDS-Desktop-QgisPlugin (공간자료 편집도구)
=======
Version 1.0 February 11th, 2019
![logo_geodt_desktop](https://user-images.githubusercontent.com/13480171/52611305-435cc180-2ec8-11e9-8366-3937725fedab.png)

이 프로젝트는 국토공간정보연구사업 중 [공간정보 SW 활용을 위한 오픈소스 가공기술 개발]과제의 5차년도 연구성과 입니다.<br>

### GeoDT Desktop 이란 무엇인가?
GeoDT는 'Geo-Spatial'과 'Design Tool'이라는 단어를 합쳐 만든 이름으로, '지리 정보를 디자인하는 도구'를 의미합니다.<br>
GeoDT Desktop는 데스크톱 환경에 설치해서 사용하는 QGIS의 플러그인이며 공간 데이터 검수를 위해서는 검수 종류, 옵션, 좌표계 등과 같은 세부 조건을 각 설정해야 합니다.<br>검수 세부 조건 설정 및 검수 수행에 관한 자세한 정보는 [사용자 매뉴얼](https://github.com/ODTBuilder/OpenGDS-Desktop-QgisPlugin/blob/master/GeoDT_web_user_guide.pdf) 또는 [GeoDT Desktop 홈페이지](http://www.geodt.co.kr/pages/desktop.html)를 참조하십시오.<br>
GeoDT Desktop는 데스크톱에서 제공하는 검수항목은 연구수행 3차년도 및 4차년도에 개발한 공간자료 검증도구 [Validator](https://github.com/ODTBuilder/Validator)와 동일합니다.<br>

### GeoDT Desktop 기능 및 특징:
- 오프라인 환경에서의 작업<br> 
GeoDT Desktop는 인터넷 연결 없이도 언제 어디서나 데스크톱을 통해 간편하게 사용할 수 있습니다.<br> 
사용자는 적합한 필터를 선택하여 편리하게 지리 정보를 관리할 수 있습니다.<br>
- 쉬운 UI<br> 
GeoDT Desktop은 지도 레이어의 검수 및 편집 기능을 지원하며, 사용자 편의를 고려한 쉽고 간편한 조작으로 사용할 수 있습니다.<br>
- 모율<br> 
GeoDT Desktop은 QGIS Desktop의 확장 플러그인입니다. QGIS에서 제공하는 기본 기능과 커뮤니티를 통해 공유되는 확장 기능을 자유롭게 조합하여 동시에 사용할 수 있습니다.<br> 
 
대표 기능
=====
### 검수 요청
![5](https://user-images.githubusercontent.com/13480171/52615071-2976ab00-2ed7-11e9-8cae-d09272055bb9.PNG)
검수를 진행하기 위해서 '환경설정' 탭에서 옵션을 설정하고 검수를 요청합니다.<br>
‘레이어 정의 옵션’ 파일과 ‘검수 옵션’ 파일은 GeoDT Web 을 통해 생성하실 수 있습니다. 자세한 내용은 공식 홈페이지(http://www.geodt.co.kr/pages/web.html#layer_setting/ )의 ‘대상 레이어 설정’ 과 ‘검수항목 세부 설정’을 참고해주세요.

### 검수 확인
 ![default](https://user-images.githubusercontent.com/13480171/52613094-fda3f700-2ecf-11e9-821d-f4f77614b23c.gif)<br>
상단 ‘Navigator’ 탭을 클릭해 검수 결과를 확인할 수 있습니다. 검수 결과는 C:/val/error 에 폴더로 저장됩니다.<br> 
이전 검수 결과를 확인하고 싶다면 ‘Verification Result’의 ‘Parent Folder’ 와 ‘Error Layer’를 설정해 원하는 검수 결과 레이어를 불러올 수 있습니다.<br>
‘Error Layer’에 보이는 표의 오류의 속성값을 클릭하면 해당 오류가 발생한 위치로 이동합니다.<br>
편집기능은 QGIS 기본기능을 사용합니다. 자세한 내용은 [QGIS 홈페이지](https://www.qgis.org/ko/site/) 를 참고하시길 바랍니다.

요구 사항
=====
### 개발 환경
- Java - OpenJDK 1.8.0.111 64 bit, JDK 1.8.0_192
- QGIS - 2.18.13

### 설치 및 연동방법
- (https://github.com/ODTBuilder/OpenGDS-Desktop-QgisPlugin/blob/master/GeoDT_desktop_user_guide.pdf)

참고 자료
=====
- [QGIS Tutorials and Tips - Building a Python Plugin](http://www.qgistutorials.com/ko/docs/building_a_python_plugin.html)

사용 라이브러리
=====

- [Validator](https://github.com/ODTBuilder/Validator) 와 동일합니다.

1. GeoTools 16.5 (LGPL) http://www.geotools.org/
2. JTS 1.12 (Eclipse Public License 1.0, Eclipse Distribution License 1.0 (a BSD Style License)) https://www.locationtech.org/
2. ApachePOI 3.14 (Apache License 2.0) http://poi.apache.org
3. ApacheCommons 1.3.3 (Apache License 2.0) commons.apache.org/proper/commons-logging/
4. JACKSON 1.9.7 (Apache License (AL) 2.0, LGPL 2.1)
5. JSON 20160212 (MIT License)
6. kabeja 0.4 (Apache Software License 2.0) http://kabeja.sourceforge.net/index.html
7. kabeja-svg 0.4 (Apache Software License 2.0) http://kabeja.sourceforge.net/index.html
8. gt-datastore-ngi 1.0.0 (GNU Library or Lesser General Public License version 2.0 (LGPLv2)) http://www.mangosystem.com/

연구기관
=====
- 연구책임 : 공간정보기술(주) <link>http://www.git.co.kr/<br>
- 협동기관 : 부산대학교 <link>http://www.pusan.ac.kr/<br>
- 주관기관 : 국토연구원 <link>http://www.krihs.re.kr/

<a name="english"></a>
OpenGDS-Desktop-QgisPlugin<br> (Geospatial Information Validation Tool)
=======
Version 1.0 February 11th, 2019
![logo_geodt_desktop](https://user-images.githubusercontent.com/13480171/52611305-435cc180-2ec8-11e9-8366-3937725fedab.png)

This project is the result of the fifth year research of "Development of open source processing technology using spatial information SW" among national spatial information research projects.

### What is GeoDT Desktop?
GeoDT is a combination of the words "Geo-Spatial"and "Design Tool", which means "tool for designing geographic information".<br> GeoDT Desktop is a QGIS plug-in that is installed and used in a desktop environment.<br> In order to perform spatial data inspection, detailed conditions such as inspection type, options, and the coordinate system must be set.<br> See the [GeoDT_Desktop v1.0-User Manual_en.pdf](https://github.com/ODTBuilder/OpenGDS-Desktop-QgisPlugin/blob/master/GeoDT_Desktop_v1.0_User_Manual_en.pdf) or the [GeoDT desktop homepage](http://www.geodt.co.kr/pages/desktop.html) for more information.<br>

### GeoDT Desktop features and functions include:
- Work in the offine environment<br> 
GeoDT Desktop is easy to use from your desktop anytime and anywhere without an internet connection.<br> 
Users can conveniently manage geographic information by selecting the appropriate filter.<br>
- Easy UI<br> 
GeoDT Desktop supports the inspection and editing of map layers and can be used easily for your convenience.<br>
- Module<br> 
GeoDT Desktop is an extension plug-in for QGIS Desktop.<br> User can use anycombination of basic functions provided by QGIS and extensions shared by the community at the same time.<br> 

GeoDT Desktop function
=====
### Running the inspection
![5](https://user-images.githubusercontent.com/13480171/52615071-2976ab00-2ed7-11e9-8cae-d09272055bb9.PNG)
To proceed with the inspection, set the options in the 'Preferences' tab and request the inspection.<br>
'Layer definition option' file and 'Review option' file can be created via GeoDT Web. 
For more information, please refer to 'Target Layer Settings'and 'Details of Inspection Items'on the official website (http://www.geodt.co.kr/pages/web.html#layer_setting/).<br>

### Inspection confirmation
![preferences](https://user-images.githubusercontent.com/20291050/68645973-13c50d80-055d-11ea-835b-903acd82ac32.png)<br>
You can check the inspection result by clicking the 'Navigator'tab at the top.<br>
The test results are stored in a folder in C:/val/error.<br>
If you want to check the previous inspection result, you can set the 'Parent Folder'and 'Error Layer'of 'Verification Result'to bring up the desired inspection result layer.<br>
Clicking on the property value of an error in the table shown in ‘Error Layer’ will take you to the location where the error occurred.<br>
The editing function uses the QGIS basic functions. For more information, please refer to the [QGIS homepage] (https://www.qgis.org/en/site/).<br>

Requirements
=====
### Development environment
- Java - OpenJDK 1.8.0.111 64 bit, JDK 1.8.0_192
- QGIS - 2.18.13

### Installation and Set up
- [GeoDT_Desktop_v1.0_User_Manual_en.pdf](https://github.com/ODTBuilder/OpenGDS-Desktop-QgisPlugin/blob/master/GeoDT_Desktop_v1.0_User_Manual_en.pdf)

Reference
=====
- [QGIS Tutorials and Tips - Building a Python Plugin](http://www.qgistutorials.com/ko/docs/building_a_python_plugin.html)

Library
=====

- [Validator](https://github.com/ODTBuilder/Validator) 

1. GeoTools 16.5 (LGPL) http://www.geotools.org/
2. JTS 1.12 (Eclipse Public License 1.0, Eclipse Distribution License 1.0 (a BSD Style License)) https://www.locationtech.org/
2. ApachePOI 3.14 (Apache License 2.0) http://poi.apache.org
3. ApacheCommons 1.3.3 (Apache License 2.0) commons.apache.org/proper/commons-logging/
4. JACKSON 1.9.7 (Apache License (AL) 2.0, LGPL 2.1)
5. JSON 20160212 (MIT License)
6. kabeja 0.4 (Apache Software License 2.0) http://kabeja.sourceforge.net/index.html
7. kabeja-svg 0.4 (Apache Software License 2.0) http://kabeja.sourceforge.net/index.html
8. gt-datastore-ngi 1.0.0 (GNU Library or Lesser General Public License version 2.0 (LGPLv2)) http://www.mangosystem.com/

Responsibility
=====
- Research responsibility : GEOSPATIAL INFORMATION TECHNOLOGY <link>http://www.git.co.kr/<br>
- Cooperative Organization : Pusan National University <link>http://www.pusan.ac.kr/<br>
- Organizer : Korea Research Institute for Human Settlements <link>http://www.krihs.re.kr/

Mail
=====
Developer : SG.LEE
ghre55@git.co.kr
