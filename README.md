[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Korean](https://img.shields.io/badge/language-Korean-blue.svg)](#korean)


<a name="korean"></a>
OpenGDS-Desktop-QgisPlugin 
=======
이 프로젝트는 국토공간정보연구사업 중 [공간정보 SW 활용을 위한 오픈소스 가공기술 개발]과제의 5차년도 연구성과 입니다.<br>
본 프로젝트는 QGIS 플러그인으로 개발되었고, 배치파일 연동을 통한 공간정보 검수를 지원합니다.<br>
배치파일은 3, 4차년도 때 Web기반으로 개발된 공간정보 검수도구인 OpenGDS(https://github.com/ODTBuilder/OpenGDS-Builder-Javascript)와 Validator(https://github.com/ODTBuilder/Validator)로 개발되었습니다. Geoserver 연동 없이 로컬파일을 직접 읽어 검수함으로써 기존 이슈였던 대용량 지원 및 고속검수가 가능합니다..<br>
또한 Web기반이 아니기 때문에 오프라인 환경에서 검수가 가능합니다.<br>

감사합니다.<br>
공간정보기술(주) 연구소 <link>http://www.git.co.kr/<br>
OpenGeoDT 팀


Getting Started
=====
### 1. 환경 ###
- Java - OpenJDK 1.8.0.111 64 bit, JDK 1.8.0_192
- QGIS - 2.18.13

### 2. 설치 및  ### 
- 설치는 [OpenGDS Desktop QGISPlugIn 매뉴얼](https://github.com/ODTBuilder/OpenGDS-Desktop-QgisPlugin/blob/master/OpenGDS%20Desktop%20QGISPlugIn%20%EB%A7%A4%EB%89%B4%EC%96%BC.docx) 을 참조하시길 바랍니다.


특징
=====
-	오프라인 환경에서의 작업<br>
GeoDT Desktop는 인터넷 연결 없이도 언제 어디서나 데스크톱을 통해 간편하게 사용할 수 있습니다. 사용자는 적합한 필터를 선택하여 편리하게 지리 정보를 관리할 수 있습니다.

-	쉬운 UI<br>
GeoDT Desktop은 지도 레이어의 검수 및 편집 기능을 지원하며, 사용자 편의를 고려한 쉽고 간편한 조작으로 사용할 수 있습니다.

-	모듈<br>
GeoDT Desktop은 QGIS Desktop의 확장 플러그인 입니다. QGIS에서 제공하는 기본 기능과 커뮤니티를 통해 공유되는 확장 기능을 자유롭게 조합하여 동시에 사용할 수 있습니다.



기능
=====
- Option 설정
  - '환경설정' 탭의 검수옵션 설정을 기반으로 QGIS 검수 옵션값을 설정함

  - 자세한 검수 옵션설정은 [GeoDT Online 웹 매뉴얼](https://github.com/ODTBuilder/OpenGDS-Desktop-QgisPlugin/blob/master/GeoDT%20Online%20%EC%9B%B9%EA%B2%80%EC%88%98%20%EB%A7%A4%EB%89%B4%EC%96%BC.hwp)을 참조하시길 바랍니다.
  
  - QGIS Parameter 연동
  ![image](https://user-images.githubusercontent.com/13480171/46720101-83a5fc00-ccaa-11e8-894c-6fb0b044ac20.JPG) 
    - 환경설정창 확대</br>
  ![1](https://user-images.githubusercontent.com/13480171/52467587-6128de80-2bc9-11e9-8072-cb1bc70d5fa5.PNG)

  - QGIS 에러 네비게이터
  ![image](https://user-images.githubusercontent.com/13480171/46720108-87d21980-ccaa-11e8-805d-374ebb668161.JPG)
    - 에러 네비게이터창 확대</br>
  ![5](https://user-images.githubusercontent.com/13480171/52467611-7dc51680-2bc9-11e9-9ca5-47994d8ba413.PNG)

연구기관
=====
- 세부 책임 : 부산대학교 <link>http://www.pusan.ac.kr/<br>
- 연구 책임 : 국토연구원 <link>http://www.krihs.re.kr/


Mail
=====
Developer : SG.LEE
ghre55@git.co.kr



