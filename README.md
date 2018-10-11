[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Korean](https://img.shields.io/badge/language-Korean-blue.svg)](#korean)
[![Englsh](https://img.shields.io/badge/language-English-orange.svg)](#english)


<a name="korean"></a>
OpenGDS-Desktop-QgisPlugin 
=======
이 프로젝트는 국토공간정보연구사업 중 [공간정보 SW 활용을 위한 오픈소스 가공기술 개발]과제의 5차년도 연구성과 입니다.<br>
QGIS 플러그인으로 개발되어졌으며, 배치파일 연동을 통한 검수를 지원한다.<br>
배치파일은 3~4차년도 때 Web기반으로 개발된 공간정보 검수도구 Java Library 기반(OpenGDS/Validator)으로 개발되어 졌으며, Geoserver연동을 통한 검수가 아닌 로컬파일을 직접 읽어 검수함으로써 기존이슈였던 대용량 지원 및 고속검수를 목적으로 한다.<br>
또한 Web기반이 아니기 때문에 오프라인 환경에서 검수가 가능하다.<br>

감사합니다.<br>
공간정보기술(주) 연구소 <link>http://www.git.co.kr/<br>
OpenGeoDT 팀


특징
=====
- 데스크톱상에서 공간정보의 기하학적/논리적 구조와 속성값에 대한 검수편집 기능을 제공함.
- python에서 Batch file호출을 통한 검수를 진행함.


기능
=====
- Option 설정
  - GeoDT Online 에서 검수옵션 설정을 기반으로 QGIS 검수 옵션값을 설정함
    - 설정 예시 1)
    
    <img width="911" alt="2018-08-24 9 15 34" src="https://user-images.githubusercontent.com/13480171/44558307-66f74880-a77e-11e8-9add-74537c569ce7.png">
    
    - 설정 예시 2)
    
    <img width="875" alt="2018-08-24 9 21 38" src="https://user-images.githubusercontent.com/13480171/44558463-3fed4680-a77f-11e8-8e86-f5bf1d327509.png">
    
    - 설정 예시 3)
   
    <img width="875" alt="2018-08-24 9 21 49" src="https://user-images.githubusercontent.com/13480171/44558462-3f54b000-a77f-11e8-91e1-d86d694faa6f.png">

  - 자세한 검수 옵션설정은 [GeoDT Online 웹 매뉴얼](https://github.com/ODTBuilder/OpenGDS-Desktop-QgisPlugin/blob/master/GeoDT%20Online%20매뉴얼.hwp)을 참조하십시오.
  
  - QGIS Parameter 연동
  ![image](https://user-images.githubusercontent.com/13480171/46720101-83a5fc00-ccaa-11e8-894c-6fb0b044ac20.JPG) 
    - 환경설정창 확대</br>
  ![image](https://user-images.githubusercontent.com/13480171/46720104-86a0ec80-ccaa-11e8-896b-a4926267ffc2.JPG)

  - QGIS 에러 네비게이터
  ![image](https://user-images.githubusercontent.com/13480171/46720108-87d21980-ccaa-11e8-805d-374ebb668161.JPG)
    - 에러 네비게이터창 확대</br>
  ![image](https://user-images.githubusercontent.com/13480171/46720113-899bdd00-ccaa-11e8-951b-5a987bf9a8c8.JPG)

연구기관
=====
- 세부 책임 : 부산대학교 <link>http://www.pusan.ac.kr/<br>
- 연구 책임 : 국토연구원 <link>http://www.krihs.re.kr/


Getting Started
=====
### 1. 환경 ###
- Java - OpenGDK 1.8.0.111 64 bit
- QGIS - 2.18.13


Mail
=====
Developer : SG.LEE
ghre55@git.co.kr



