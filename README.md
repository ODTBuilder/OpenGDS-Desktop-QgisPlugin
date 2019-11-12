[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Korean](https://img.shields.io/badge/language-Korean-blue.svg)](#korean)


<a name="korean"></a>
OpenGDS-Desktop-QgisPlugin (공간자료 편집도구)
=======
Version 1.0 February 11th, 2019
![logo_geodt_desktop](https://user-images.githubusercontent.com/13480171/52611305-435cc180-2ec8-11e9-8366-3937725fedab.png)


이 프로젝트는 국토공간정보연구사업 중 [공간정보 SW 활용을 위한 오픈소스 가공기술 개발]과제의 5차년도 연구성과 입니다.<br>
본 프로젝트는 QGIS 플러그인으로 개발되었고, 배치파일 연동을 통한 공간정보 검수를 지원합니다.<br>

검수기능은 3, 4차년도 때 Web기반으로 개발된 공간정보 검수도구인 [Validator](https://github.com/ODTBuilder/Validator)로 개발되었습니다.

Geoserver 연동 없이 로컬파일을 직접 읽어 검수함으로써 기존 이슈였던 대용량 지원, 고속 검수 및 편집을 지원합니다.<br>
또한 Web기반이 아니기 때문에 오프라인 환경에서 검수가 가능합니다.
자세한 검수 옵션설정은 [GeoDT Online 웹 매뉴얼](https://github.com/ODTBuilder/OpenGDS-Desktop-QgisPlugin/blob/master/GeoDT_web_user_guide.pdf)을 참고하시길 바랍니다.

또한 [GeoDT Desktop 홈페이지](http://www.geodt.co.kr/pages/desktop.html)도 제공하고 있으니 참고바랍니다.

감사합니다.<br>
공간정보기술(주) 연구소 <link>http://www.git.co.kr/<br>
OpenGeoDT 팀

연구기관
=====
- 세부 책임 : 부산대학교 <link>http://www.pusan.ac.kr/<br>
- 연구 책임 : 국토연구원 <link>http://www.krihs.re.kr/

#
### 목차
    
  - [기능 소개](#기능-소개)  
    - [검수요청](#검수요청)
    - [오류 객체 추적](#오류-객체-추적)
  - [요구 사항](#요구-사항) 
  - [참고 자료](#참고-자료)
  - [사용 라이브러리](#사용-라이브러리)
 
기능 소개
=====
## 검수요청

  ![5](https://user-images.githubusercontent.com/13480171/52615071-2976ab00-2ed7-11e9-8cae-d09272055bb9.PNG)
   검수를 진행하기 위해서 옵션 값을 설정하고 검수를 요청합니다. '환경설정' 탭의 검수옵션 설정을 기반으로 QGIS 검수 옵션값을 설정합니다.<br>
   검수 옵션 파일(레이어 정의 옵션, 검수 경로 옵션) 은 [GeoDT Web](http://www.geodt.co.kr/pages/web.html) 을 통해 만들 수 있습니다. GeoDT Web의 사용 방법은 매뉴얼인 [GeoDT_web_user_guide.doc](https://github.com/ODTBuilder/OpenGDS-Desktop-QgisPlugin/blob/master/GeoDT_web_user_guide.pdf) 을 참고하시길 바랍니다.


## 오류 객체 추적

 ![default](https://user-images.githubusercontent.com/13480171/52613094-fda3f700-2ecf-11e9-821d-f4f77614b23c.gif)<br>
 검수가 완료되면 네비게이터를 통해 오류목록을 볼 수 있습니다. 오류 항목을 클릭하면 오류 객체를 추적해 해당 위치로 QGIS 맵이 이동합니다.
 <br>편집기능은 QGIS 기본기능을 사용합니다. 자세한 내용은 [QGIS 홈페이지](https://www.qgis.org/ko/site/) 를 참고하시길 바랍니다.

  
요구 사항
=====
### 1. 환경 ###
- Java - OpenJDK 1.8.0.111 64 bit, JDK 1.8.0_192
- QGIS - 2.18.13

### 2. 설치 및 연동방법 ### 
- 설치 및 연동방법은 매뉴얼인 [GeoDT_desktop_user_guide.docx](https://github.com/ODTBuilder/OpenGDS-Desktop-QgisPlugin/blob/master/GeoDT_desktop_user_guide.pdf) 을 참고하시길 바랍니다.

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


<a name="english"></a>
OpenGDS-Desktop-QgisPlugin<br> (Geospatial Information Validation Tool)
=======
Version 1.0 February 11th, 2019
![logo_geodt_desktop](https://user-images.githubusercontent.com/13480171/52611305-435cc180-2ec8-11e9-8366-3937725fedab.png)

### What is GeoDT Desktop?
GeoDT is a combination of the words "Geo-Spatial"and "Design Tool", which means "tool for designing geographic information".<br> 
GeoDT Desktop is a QGIS plug-in that is installed and used in a desktop environment.<br>  
In order to perform spatial data inspection, detailed conditions such as inspection type, options, and the coordinate system must be set.<br> 

### GeoDT Desktop features and functions include:
- Work in the offine environment<br> 
GeoDT Desktop is easy to use from your desktop anytime and anywhere without an internet connection.<br> 
Users can conveniently manage geographic information by selecting the appropriate filter.<br>
- Easy UI<br> 
GeoDT Desktop supports the inspection and editing of map layers and can be used easily for your convenience.<br>
- Module<br> 
GeoDT Desktop is an extension plug-in for QGIS Desktop.<br> User can use anycombination of basic functions provided by QGIS and extensions shared by the community at the same time.


Mail
=====
Developer : SG.LEE
ghre55@git.co.kr



