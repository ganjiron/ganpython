from html.parser import HTMLParser

from bs4 import BeautifulSoup

html_doc = '''<!DOCTYPE html>
<html lang="ko" dir="ltr">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="shortcut icon" href="https://cse.snu.ac.kr/sites/all/themes/dcse/favicon.ico" type="image/vnd.microsoft.icon" />
<link rel="alternate" type="application/rss+xml" title="공지사항" href="https://cse.snu.ac.kr/department-notices.xml" />
<link rel="alternate" type="application/rss+xml" title="새소식" href="https://cse.snu.ac.kr/news.xml" />
<meta name="Generator" content="Drupal 7 (http://drupal.org)" />
    <title>서울대학교 컴퓨터공학부</title>
    <link type="text/css" rel="stylesheet" href="https://cse.snu.ac.kr/sites/default/files/css/css_fv_Aqxc-TFlMJfHYNW_3F7bTydnFUHTU2FAOYKgVQ6o.css" media="all" />
<link type="text/css" rel="stylesheet" href="https://cse.snu.ac.kr/sites/default/files/css/css_aPlVzOTIqeTpwJwee_6zfAIHJnVVCcT2yrpnsRMKc0M.css" media="all" />
<link type="text/css" rel="stylesheet" href="https://cse.snu.ac.kr/sites/default/files/css/css_d2lMouZ7O8cp7ttRnfcm9VKEEZgyI5M66c1QzKhQN8Q.css" media="all" />
<link type="text/css" rel="stylesheet" href="https://cse.snu.ac.kr/sites/default/files/css/css_tKI1-CCEkII6MT3trUnXLD2LJb9PLotY0skEgRQTfwQ.css" media="all" />
<link type="text/css" rel="stylesheet" href="https://cse.snu.ac.kr/sites/default/files/css/css_dn8VFLuxReMiP3WgqX0JDHyvUuwTp9Lu09YUG3nLbSY.css" media="print" />

<!--[if lte IE 8]>
<link type="text/css" rel="stylesheet" href="https://cse.snu.ac.kr/sites/default/files/css/css_RjdLjrH38JQ9GKB8D7hBv7QwLKjAZUuyNjD7CwdeyF8.css" media="all" />
<![endif]-->
		<meta name="google-translate-customization" content="6a6d90d7527df5b2-d0c482b2e806f2cb-g4c306c95986efc1f-e"></meta>
  </head>
  <body class="html front not-logged-in no-sidebars page-home i18n-ko">
    <div id="skip-link">
      <a href="#navigation" class="element-invisible element-focusable">내비게이션으로 건너뛰기</a>
    </div><!-- // -->
        <div id="page-wrapper"><div id="page">

  <div id="header">
		<div id="header-top"><div class="section">
		  <div id="menu-wrapper">
   	    					<div id="login-block" class="block"><a href="/user/login">로그인</a></div>
	      	      	        <div class="region region-secondary">
    <div id="block-locale-language" class="block block-locale first last odd">


  <div class="content">
    <ul class="language-switcher-locale-url"><li class="ko first active"><a href="/" class="language-link active">한국어</a></li>
<li class="en last"><a href="/en" class="language-link">English</a></li>
</ul>  </div>

</div><!-- /.block -->
  </div><!-- /.region -->
	    </div> <!-- /#menu-wrapper/ -->
		</div></div> <!-- /.section /.header-top -->
  <div class="section">
    <div id="site-logo">
      <div id="logo-background"></div>
      <a href="/" title="홈" rel="home"><img src="https://cse.snu.ac.kr/sites/all/themes/dcse/images/logo-ko.png" alt="홈" width='364' height='87' /></a>
    </div>
    <div class="element-invisible">
                        <h1 id="site-name">
            <a href="/" title="홈" rel="home"><span>서울대학교 컴퓨터공학부</span></a>
          </h1>


    </div><!-- /.element-invisible -->
      <div class="region region-search-box">
    <div id="block-search-form" class="block block-search first last odd">


  <div class="content">
    <form action="/" method="post" id="search-block-form" accept-charset="UTF-8"><div><div class="container-inline">
      <h2 class="element-invisible">검색 폼</h2>
    <div class="form-item form-type-textfield form-item-search-block-form">  <label class="element-invisible" for="edit-search-block-form--2">검색 </label> <input title="찾고자 하는 단어를 입력하십시오" placeholder="검색" type="text" id="edit-search-block-form--2" name="search_block_form" value="" size="15" maxlength="128" class="form-text" /></div><div class="form-actions form-wrapper" id="edit-actions"><input type="submit" id="edit-submit" name="op" value="검색" class="form-submit" /></div><input type="hidden" name="form_build_id" value="form-KCcCQedhPuF_6-3vKOx7dTLjB-7kNZaMqjPENPvFF2Y" />
<input type="hidden" name="form_id" value="search_block_form" />
</div>
</div></form>  </div>

</div><!-- /.block -->
  </div><!-- /.region -->


  <div id="navigation-links">
      <div class="region region-navigation">
    <div id="block-superfish-1" class="block block-superfish first last odd">


  <div class="content">
    <ul id="superfish-1" class="sf-menu main-menu sf-horizontal sf-style-none sf-total-items-7 sf-parent-items-7 sf-single-items-0"><li id="menu-256-1" class="first odd sf-item-1 sf-depth-1 sf-total-children-8 sf-parent-children-1 sf-single-children-7 menuparent"><a href="/about" class="sf-depth-1  menuparent">소개</a><ul><li id="menu-766-1" class="first odd sf-item-1 sf-depth-2 sf-no-children"><a href="/about" title="" class="sf-depth-2 ">학부 소개</a></li><li id="menu-1637-1" class="middle even sf-item-2 sf-depth-2 sf-no-children"><a href="/greetings" title="" class="sf-depth-2 ">학부장 인사말</a></li><li id="menu-4135-1" class="middle odd sf-item-3 sf-depth-2 sf-no-children"><a href="/history" class="sf-depth-2 ">연혁</a></li><li id="menu-1734-1" class="middle even sf-item-4 sf-depth-2 sf-no-children"><a href="/career-options" title="" class="sf-depth-2 ">졸업생 진로</a></li><li id="menu-3046-1" class="middle odd sf-item-5 sf-depth-2 sf-no-children"><a href="/student-clubs" title="" class="sf-depth-2 ">동아리 소개</a></li><li id="menu-1631-1" class="middle even sf-item-6 sf-depth-2 sf-no-children"><a href="/facilities" title="" class="sf-depth-2 ">시설 안내</a></li><li id="menu-302-1" class="middle odd sf-item-7 sf-depth-2 sf-no-children"><a href="/contact-us" class="sf-depth-2 ">연락처</a></li><li id="menu-299-1" class="last even sf-item-8 sf-depth-2 sf-total-children-3 sf-parent-children-0 sf-single-children-3 menuparent"><a href="/directions" class="sf-depth-2  menuparent">찾아오는 길</a><ul><li id="menu-1171-1" class="first odd sf-item-1 sf-depth-3 sf-no-children"><a href="/directions/by-public-transit" class="sf-depth-3 ">대중교통</a></li><li id="menu-1169-1" class="middle even sf-item-2 sf-depth-3 sf-no-children"><a href="/directions/by-car" class="sf-depth-3 ">승용차</a></li><li id="menu-1170-1" class="last odd sf-item-3 sf-depth-3 sf-no-children"><a href="/directions/from-far-away" class="sf-depth-3 ">지방 및 해외</a></li></ul></li></ul></li><li id="menu-3376-1" class="middle even sf-item-2 sf-depth-1 sf-total-children-3 sf-parent-children-0 sf-single-children-3 menuparent"><a href="/people" class="sf-depth-1  menuparent">구성원</a><ul><li id="menu-328-1" class="first odd sf-item-1 sf-depth-2 sf-no-children"><a href="/people/faculty" title="" class="sf-depth-2 ">교수진</a></li><li id="menu-2957-1" class="middle even sf-item-2 sf-depth-2 sf-no-children"><a href="/people/emeritus-faculty" title="" class="sf-depth-2 ">역대 교수진</a></li><li id="menu-500-1" class="last odd sf-item-3 sf-depth-2 sf-no-children"><a href="/people/staff" title="" class="sf-depth-2 ">행정직원</a></li></ul></li><li id="menu-3347-1" class="middle odd sf-item-3 sf-depth-1 sf-total-children-4 sf-parent-children-0 sf-single-children-4 menuparent"><a href="/research" class="sf-depth-1  menuparent">연구</a><ul><li id="menu-652-1" class="first odd sf-item-1 sf-depth-2 sf-no-children"><a href="/research/groups" title="" class="sf-depth-2 ">연구 그룹</a></li><li id="menu-650-1" class="middle even sf-item-2 sf-depth-2 sf-no-children"><a href="/research/centers" title="" class="sf-depth-2 ">연구 센터</a></li><li id="menu-3353-1" class="middle odd sf-item-3 sf-depth-2 sf-no-children"><a href="/research/labs" title="" class="sf-depth-2 ">연구실 목록</a></li><li id="menu-4248-1" class="last even sf-item-4 sf-depth-2 sf-no-children"><a href="/node/29041" title="" class="sf-depth-2 ">CSE Top Conference List</a></li></ul></li><li id="menu-1167-1" class="middle even sf-item-4 sf-depth-1 sf-total-children-2 sf-parent-children-2 sf-single-children-0 menuparent"><a href="/admissions" class="sf-depth-1  menuparent">입학</a><ul><li id="menu-3852-1" class="first odd sf-item-1 sf-depth-2 sf-total-children-3 sf-parent-children-0 sf-single-children-3 menuparent"><a href="/admissions/undergraduate" class="sf-depth-2  menuparent">학부</a><ul><li id="menu-662-1" class="first odd sf-item-1 sf-depth-3 sf-no-children"><a href="/admissions/undergraduate/susi" class="sf-depth-3 ">수시 모집</a></li><li id="menu-663-1" class="middle even sf-item-2 sf-depth-3 sf-no-children"><a href="/admissions/undergraduate/jeongsi" class="sf-depth-3 ">정시 모집</a></li><li id="menu-669-1" class="last odd sf-item-3 sf-depth-3 sf-no-children"><a href="/admissions/transfer" class="sf-depth-3 ">학사 편입학</a></li></ul></li><li id="menu-3851-1" class="last even sf-item-2 sf-depth-2 sf-total-children-1 sf-parent-children-0 sf-single-children-1 menuparent"><a href="/admissions/graduate" class="sf-depth-2  menuparent">대학원</a><ul><li id="menu-657-1" class="first odd sf-item-1 sf-depth-3 sf-no-children"><a href="/admissions/graduate/regular" class="sf-depth-3 ">전기/후기 모집</a></li></ul></li></ul></li><li id="menu-3339-1" class="middle odd sf-item-5 sf-depth-1 sf-total-children-3 sf-parent-children-2 sf-single-children-1 menuparent"><a href="/department-notices" title="" class="sf-depth-1  menuparent">학사 및 교과</a><ul><li id="menu-3340-1" class="first odd sf-item-1 sf-depth-2 sf-no-children"><a href="/department-notices" title="" class="sf-depth-2 ">공지사항</a></li><li id="menu-1212-1" class="middle even sf-item-2 sf-depth-2 sf-total-children-7 sf-parent-children-0 sf-single-children-7 menuparent"><a href="/undergraduate" class="sf-depth-2  menuparent">학부</a><ul><li id="menu-3330-1" class="first odd sf-item-1 sf-depth-3 sf-no-children"><a href="/undergraduate/courses" title="" class="sf-depth-3 ">교과목 정보</a></li><li id="menu-2784-1" class="middle even sf-item-2 sf-depth-3 sf-no-children"><a href="/undergraduate/course-dependency-graph" class="sf-depth-3 ">선수 교과목</a></li><li id="menu-3334-1" class="middle odd sf-item-3 sf-depth-3 sf-no-children"><a href="/undergraduate/recommended-tracks" title="" class="sf-depth-3 ">전공 이수 표준 형태</a></li><li id="menu-2691-1" class="middle even sf-item-4 sf-depth-3 sf-no-children"><a href="/undergraduate/general-education-requirements" class="sf-depth-3 ">필수 교양 과목</a></li><li id="menu-3342-1" class="middle odd sf-item-5 sf-depth-3 sf-no-children"><a href="/undergraduate/degree-requirements" title="" class="sf-depth-3 ">졸업 규정</a></li><li id="menu-3992-1" class="middle even sf-item-6 sf-depth-3 sf-no-children"><a href="/undergraduate/course-changes" class="sf-depth-3 ">교과목 변경 내역</a></li><li id="menu-3042-1" class="last odd sf-item-7 sf-depth-3 sf-no-children"><a href="/undergraduate/scholarships" class="sf-depth-3 ">장학제도</a></li></ul></li><li id="menu-1213-1" class="last odd sf-item-3 sf-depth-2 sf-total-children-3 sf-parent-children-0 sf-single-children-3 menuparent"><a href="/graduate" class="sf-depth-2  menuparent">대학원</a><ul><li id="menu-3332-1" class="first odd sf-item-1 sf-depth-3 sf-no-children"><a href="/graduate/courses" title="" class="sf-depth-3 ">교과목 정보</a></li><li id="menu-3993-1" class="middle even sf-item-2 sf-depth-3 sf-no-children"><a href="/graduate/course-changes" class="sf-depth-3 ">교과목 변경 내역</a></li><li id="menu-3043-1" class="last odd sf-item-3 sf-depth-3 sf-no-children"><a href="/graduate/scholarships" class="sf-depth-3 ">장학제도</a></li></ul></li></ul></li><li id="menu-1300-1" class="middle even sf-item-6 sf-depth-1 sf-total-children-2 sf-parent-children-2 sf-single-children-0 menuparent"><a href="/online-services" class="sf-depth-1  menuparent">온라인 서비스</a><ul><li id="menu-751-1" class="first odd sf-item-1 sf-depth-2 sf-total-children-8 sf-parent-children-0 sf-single-children-8 menuparent"><a href="/seminar-room-reservations" class="sf-depth-2  menuparent">세미나실 예약</a><ul><li id="menu-2705-1" class="first odd sf-item-1 sf-depth-3 sf-no-children"><a href="/301-417" class="sf-depth-3 ">301-417 (28석)</a></li><li id="menu-2706-1" class="middle even sf-item-2 sf-depth-3 sf-no-children"><a href="/301-551" class="sf-depth-3 ">301-551 (42석)</a></li><li id="menu-4251-1" class="middle odd sf-item-3 sf-depth-3 sf-no-children"><a href="/302-209" class="sf-depth-3 ">302-209 (48석)</a></li><li id="menu-2707-1" class="middle even sf-item-4 sf-depth-3 sf-no-children"><a href="/302-308" title="Study Visit from University of Technology in Delft" class="sf-depth-3 ">302-308 (46석)</a></li><li id="menu-3991-1" class="middle odd sf-item-5 sf-depth-3 sf-no-children"><a href="/302-309" class="sf-depth-3 ">302-309 (36석)</a></li><li id="menu-2708-1" class="middle even sf-item-6 sf-depth-3 sf-no-children"><a href="/302-309-1" class="sf-depth-3 ">302-309-1 (45석)</a></li><li id="menu-3127-1" class="middle odd sf-item-7 sf-depth-3 sf-no-children"><a href="/301-317" class="sf-depth-3 ">301-317 교수회의실 (30석)</a></li><li id="menu-3128-1" class="last even sf-item-8 sf-depth-3 sf-no-children"><a href="/302-317-3" class="sf-depth-3 ">302-317-3 교수회의실 (8석)</a></li></ul></li><li id="menu-4218-1" class="last even sf-item-2 sf-depth-2 sf-total-children-2 sf-parent-children-0 sf-single-children-2 menuparent"><a href="/lab-reservations" class="sf-depth-2  menuparent">실습실 예약</a><ul><li id="menu-4219-1" class="first odd sf-item-1 sf-depth-3 sf-no-children"><a href="/302-311-1" class="sf-depth-3 ">소프트웨어실습실 (64석)</a></li><li id="menu-4220-1" class="last even sf-item-2 sf-depth-3 sf-no-children"><a href="/302-310-2" class="sf-depth-3 ">하드웨어실습실 (30석)</a></li></ul></li></ul></li><li id="menu-4245-1" class="last odd sf-item-7 sf-depth-1 sf-total-children-1 sf-parent-children-0 sf-single-children-1 menuparent"><a href="/faculty-recruitment" class="sf-depth-1  menuparent">신임교수초빙</a><ul><li id="menu-4247-1" class="first odd sf-item-1 sf-depth-2 sf-no-children"><a href="/faculty-recruitment" title="" class="sf-depth-2 ">신임교수초빙</a></li></ul></li></ul>  </div>

</div><!-- /.block -->
  </div><!-- /.region -->
  </div><!-- /#navigation-links -->



  </div></div><!-- /.section, /#header -->

  <div id="main"><div class="section clearfix2">
                	<div id="slideshow"><div class="section clearfix2">
	    <div class="region region-slideshow">
    <div id="block-views-slideshow-slideshow" class="block block-views first last odd">


  <div class="content">
    <div class="view view-slideshow view-id-slideshow view-display-id-slideshow view-dom-id-0de5f9eb56a2d2646719ae31d4eafae6">



      <div class="view-content">
      <div class="skin-default">
  <div id="views_slideshow_cycle_main_slideshow-slideshow" class="views_slideshow_cycle_main views_slideshow_main"><div id="views_slideshow_cycle_teaser_section_slideshow-slideshow" class="views-slideshow-cycle-main-frame views_slideshow_cycle_teaser_section">
  <div id="views_slideshow_cycle_div_slideshow-slideshow_0" class="views-slideshow-cycle-main-frame-row views_slideshow_cycle_slide views_slideshow_slide views-row-1 views-row-odd">
  <div class="views-slideshow-cycle-main-frame-row-item views-row views-row-0 views-row-first views-row-odd">

  <div class="views-field views-field-title">        <span class="field-content"><a href="/node/33185">2018년 8월 우수학위논문상 수상자 안내</a></span>  </div>
  <div class="views-field views-field-field-main-image">        <div class="field-content"><a href="/node/33185"><img src="https://cse.snu.ac.kr/sites/default/files/styles/medium-landscape-crop/public/node--news/tree_0_1_0_0_0.jpg" width="220" height="140" alt="" /></a></div>  </div>
  <div class="views-field views-field-body">        <div class="field-content"><p>서울대학교 컴퓨터공학부에서는 매 학기 졸업생을 대상으로 우수학위논문상을 수여합니다.
<br /><br /></p></div>  </div>
  <div class="views-field views-field-view-node">        <span class="field-content"><a href="/node/33185">더 보기</a></span>  </div></div>
<div class="views-slideshow-cycle-main-frame-row-item views-row views-row-1 views-row-even">

  <div class="views-field views-field-title">        <span class="field-content"><a href="/node/32702">하순회 교수 연구진, LPIRC 2018에서 우수한 성적 거둬</a></span>  </div>
  <div class="views-field views-field-field-main-image">        <div class="field-content"><a href="/node/32702"><img src="https://cse.snu.ac.kr/sites/default/files/styles/medium-landscape-crop/public/node--news/_%EB%9E%A9%EC%84%B8%EB%AF%B8%EB%82%98.jpg" width="220" height="140" alt="" /></a></div>  </div>
  <div class="views-field views-field-body">        <div class="field-content"><p>하순회 교수 연구진이 저전력 이미지 인식 대회인 LPIRC에서 작년에 이어, 올해에도 1~2등상을 수상하였습니다.
</p>
<!-- Tidy found serious XHTML errors --></div>  </div>
  <div class="views-field views-field-view-node">        <span class="field-content"><a href="/node/32702">더 보기</a></span>  </div></div>
<div class="views-slideshow-cycle-main-frame-row-item views-row views-row-2 views-row-odd">

  <div class="views-field views-field-title">        <span class="field-content"><a href="/node/32239">송현오 교수 연구진, 빠르고 정확한 데이터 검색을 위한 deep binary representation learning 알고리즘 고안</a></span>  </div>
  <div class="views-field views-field-field-main-image">        <div class="field-content"><a href="/node/32239"><img src="https://cse.snu.ac.kr/sites/default/files/styles/medium-landscape-crop/public/node--news/_301%EB%8F%99%EA%B1%B4%EB%AC%BC%20%EB%82%B4%EB%B6%80_small%282%29_0.jpg" width="220" height="140" alt="" /></a></div>  </div>
  <div class="views-field views-field-body">        <div class="field-content"><p>머신러닝 분야 최고 학회인 ICML 2018에 송현오 교수 연구진의 논문이 게재되었습니다.
</p>
<!-- Tidy found serious XHTML errors --></div>  </div>
  <div class="views-field views-field-view-node">        <span class="field-content"><a href="/node/32239">더 보기</a></span>  </div></div>
<div class="views-slideshow-cycle-main-frame-row-item views-row views-row-3 views-row-even">

  <div class="views-field views-field-title">        <span class="field-content"><a href="/node/32178">바이오지능연구실 SnuBiVtt, AI 국제대회에서 1등상 수상</a></span>  </div>
  <div class="views-field views-field-field-main-image">        <div class="field-content"><a href="/node/32178"><img src="https://cse.snu.ac.kr/sites/default/files/styles/medium-landscape-crop/public/node--news/_%EC%9E%A5%EB%B3%91%ED%83%81%25252520%EA%B5%90%EC%88%98%25252520%EC%97%B0%EA%B5%AC%ED%8C%80.jpg" width="220" height="140" alt="" /></a></div>  </div>
  <div class="views-field views-field-body">        <div class="field-content"><p>바이오 지능 연구실의 '스누비Vtt' 팀이 2018 북미컴퓨터언어학회 '시각 스토리텔링 챌린지 대회'에서 1등을 차지했습니다.
</p>
<!-- Tidy found serious XHTML errors --></div>  </div>
  <div class="views-field views-field-view-node">        <span class="field-content"><a href="/node/32178">더 보기</a></span>  </div></div>
</div>
<div id="views_slideshow_cycle_div_slideshow-slideshow_1" class="views-slideshow-cycle-main-frame-row views_slideshow_cycle_slide views_slideshow_slide views-row-2 views_slideshow_cycle_hidden views-row-even">
  <div class="views-slideshow-cycle-main-frame-row-item views-row views-row-0 views-row-first views-row-odd">

  <div class="views-field views-field-title">        <span class="field-content"><a href="/node/32041">이제희교수 연구진, POSNA에서 &#039;기초 논문 본상&#039; 수상</a></span>  </div>
  <div class="views-field views-field-field-main-image">        <div class="field-content"><a href="/node/32041"><img src="https://cse.snu.ac.kr/sites/default/files/styles/medium-landscape-crop/public/node--news/_CID_ii_1606766374f0622f_CID_lab_loco.JPG" width="220" height="140" alt="" /></a></div>  </div>
  <div class="views-field views-field-body">        <div class="field-content"><p>이제희교수-서울의대 공동연구팀이 북미소아정형외과학회(POSNA)에서 기초 논문 본상을 수상하였습니다.
</p>
<!-- Tidy found serious XHTML errors --></div>  </div>
  <div class="views-field views-field-view-node">        <span class="field-content"><a href="/node/32041">더 보기</a></span>  </div></div>
<div class="views-slideshow-cycle-main-frame-row-item views-row views-row-1 views-row-even">

  <div class="views-field views-field-title">        <span class="field-content"><a href="/node/32021">컴퓨터과학의 원천 아이디어가 나오기까지</a></span>  </div>
  <div class="views-field views-field-field-main-image">        <div class="field-content"><a href="/node/32021"><img src="https://cse.snu.ac.kr/sites/default/files/styles/medium-landscape-crop/public/node--news/kaos.jpg" width="220" height="140" alt="" /></a></div>  </div>
  <div class="views-field views-field-body">        <div class="field-content"><p>과학기술 나눔재단에서 진행한 이광근 교수님의 강연 '컴퓨터과학의 원천 아이디어가 나오기까지'를 소개합니다.
</p>
<!-- Tidy found serious XHTML errors --></div>  </div>
  <div class="views-field views-field-view-node">        <span class="field-content"><a href="/node/32021">더 보기</a></span>  </div></div>
<div class="views-slideshow-cycle-main-frame-row-item views-row views-row-2 views-row-odd">

  <div class="views-field views-field-title">        <span class="field-content"><a href="/node/31237">2018년 제1차 컴퓨터공학부 교수채용 안내</a></span>  </div>
  <div class="views-field views-field-field-main-image">        <div class="field-content"><a href="/node/31237"><img src="https://cse.snu.ac.kr/sites/default/files/styles/medium-landscape-crop/public/node--news/_%EC%A0%84%EB%A9%B4_small.jpg" width="220" height="140" alt="" /></a></div>  </div>
  <div class="views-field views-field-body">        <div class="field-content"><p>서울대학교 컴퓨터공학부는 컴퓨터 미래 기술 분야의 신규 교원을 채용합니다.
</p>
<!-- Tidy found serious XHTML errors --></div>  </div>
  <div class="views-field views-field-view-node">        <span class="field-content"><a href="/node/31237">더 보기</a></span>  </div></div>
<div class="views-slideshow-cycle-main-frame-row-item views-row views-row-3 views-row-even">

  <div class="views-field views-field-title">        <span class="field-content"><a href="/node/31800">박근수.이재진 교수 연구실, 2018년 SW스타랩에 선정</a></span>  </div>
  <div class="views-field views-field-field-main-image">        <div class="field-content"><a href="/node/31800"><img src="https://cse.snu.ac.kr/sites/default/files/styles/medium-landscape-crop/public/node--news/_301.2%EB%8F%99%EA%B1%B4%EB%AC%BC%20%EC%99%B8%EB%B6%80_small%282%29_1.jpg" width="220" height="140" alt="" /></a></div>  </div>
  <div class="views-field views-field-body">        <div class="field-content"><p>'2018년 SW스타랩'에 박근수교수 연구실(알고리즘)과 이재진교수 연구실(분산컴퓨팅)이 선정되었습니다.
</p>
<!-- Tidy found serious XHTML errors --></div>  </div>
  <div class="views-field views-field-view-node">        <span class="field-content"><a href="/node/31800">더 보기</a></span>  </div></div>
</div>
<div id="views_slideshow_cycle_div_slideshow-slideshow_2" class="views-slideshow-cycle-main-frame-row views_slideshow_cycle_slide views_slideshow_slide views-row-3 views_slideshow_cycle_hidden views-row-odd">
  <div class="views-slideshow-cycle-main-frame-row-item views-row views-row-0 views-row-first views-row-odd">

  <div class="views-field views-field-title">        <span class="field-content"><a href="/node/15752">신공학관 3층 해동학술정보실 이용 안내</a></span>  </div>
  <div class="views-field views-field-field-main-image">        <div class="field-content"><a href="/node/15752"><img src="https://cse.snu.ac.kr/sites/default/files/styles/medium-landscape-crop/public/node--news/_%ED%95%B4%EB%8F%99%EB%8F%84%EC%84%9C%EA%B4%802.JPG" width="220" height="140" alt="" /></a></div>  </div>
  <div class="views-field views-field-body">        <div class="field-content"><p>301동 해동학술정보실에 대한 학생 여러분의 많은 관심과 이용 바랍니다(자료실 운영: 월~금, 9:00 ~ 18:00).
</p>
<!-- Tidy found serious XHTML errors --></div>  </div>
  <div class="views-field views-field-view-node">        <span class="field-content"><a href="/node/15752">더 보기</a></span>  </div></div>
<div class="views-slideshow-cycle-main-frame-row-item views-row views-row-1 views-row-even">

  <div class="views-field views-field-title">        <span class="field-content"><a href="/node/30484">전병곤교수 연구진의 Nemo, ASF 오픈소스 인큐베이션 프로젝트로 선정</a></span>  </div>
  <div class="views-field views-field-field-main-image">        <div class="field-content"><a href="/node/30484"><img src="https://cse.snu.ac.kr/sites/default/files/styles/medium-landscape-crop/public/node--news/_2018%EB%B2%84%EC%A0%BC.jpg" width="220" height="140" alt="" /></a></div>  </div>
  <div class="views-field views-field-body">        <div class="field-content"><p>빅데이터 분석 시스템 ‘네모(Nemo)’가 아파치소프트웨어재단(ASF)으로부터 오픈소스 프로젝트 인큐베이션을 승인받았습니다.
</p>
<!-- Tidy found serious XHTML errors --></div>  </div>
  <div class="views-field views-field-view-node">        <span class="field-content"><a href="/node/30484">더 보기</a></span>  </div></div>
<div class="views-slideshow-cycle-main-frame-row-item views-row views-row-2 views-row-odd">

  <div class="views-field views-field-title">        <span class="field-content"><a href="/node/30230">제 24회 휴먼테크논문대상 CSE 분야 1등상 수상</a></span>  </div>
  <div class="views-field views-field-field-main-image">        <div class="field-content"><a href="/node/30230"><img src="https://cse.snu.ac.kr/sites/default/files/styles/medium-landscape-crop/public/node--news/_%EC%98%A4%EC%84%B8%EC%A4%80.jpeg" width="220" height="140" alt="" /></a></div>  </div>
  <div class="views-field views-field-body">        <div class="field-content"><p>제 24회 휴먼테크논문대상 CSE분야에서 오세준 학부생이 1등을, 장준기 대학원생이 4등을 차지하였습니다.
</p>
<!-- Tidy found serious XHTML errors --></div>  </div>
  <div class="views-field views-field-view-node">        <span class="field-content"><a href="/node/30230">더 보기</a></span>  </div></div>
<div class="views-slideshow-cycle-main-frame-row-item views-row views-row-3 views-row-even">

  <div class="views-field views-field-title">        <span class="field-content"><a href="/node/29416">김건희 교수 연구진, MSRA 공동연구 지원 프로그램 선정</a></span>  </div>
  <div class="views-field views-field-field-main-image">        <div class="field-content"><a href="/node/29416"><img src="https://cse.snu.ac.kr/sites/default/files/styles/medium-landscape-crop/public/node--news/_301%EB%8F%99%EA%B1%B4%EB%AC%BC%20%EB%82%B4%EB%B6%80_small%282%29.jpg" width="220" height="140" alt="" /></a></div>  </div>
  <div class="views-field views-field-body">        <div class="field-content"><p>김건희 교수 연구진이 올해 11월 MSRA Collaborative Research 2018 Awards의 대상자로 선정되었습니다.
</p>
<!-- Tidy found serious XHTML errors --></div>  </div>
  <div class="views-field views-field-view-node">        <span class="field-content"><a href="/node/29416">더 보기</a></span>  </div></div>
</div>
</div>
</div>      <div class="views-slideshow-controls-bottom clearfix">
      <div id="views_slideshow_controls_text_slideshow-slideshow" class="views-slideshow-controls-text views_slideshow_controls_text">
  <span id="views_slideshow_controls_text_previous_slideshow-slideshow" class="views-slideshow-controls-text-previous views_slideshow_controls_text_previous"><a href="#">Previous</a></span>
  <span id="views_slideshow_controls_text_pause_slideshow-slideshow" class="views-slideshow-controls-text-pause views_slideshow_controls_text_pause"><a href="#">Pause</a></span>
  <span id="views_slideshow_controls_text_next_slideshow-slideshow" class="views-slideshow-controls-text-next views_slideshow_controls_text_next"><a href="#">다음</a></span>
</div>
    </div>
  </div>
    </div>






</div>  </div>

</div><!-- /.block -->
  </div><!-- /.region -->
	</div></div><!-- /.section, /#slideshow -->
            	<div id="top-user-regions"><div class="section clearfix2">
	    <div class="region region-user1">
    <div id="block-views-notices-block-1" class="block block-views first odd">


  <div class="content">
    <div class="view view-notices view-id-notices view-display-id-block_1 view-dom-id-441b5789edbbfb38e4e5ad7cd01f2323">



      <div class="view-content">
        <div class="views-row views-row-1 views-row-odd views-row-first">

  <div class="views-field views-field-field-main-title">        <h3 class="field-content"><a href="/node/32773">컴퓨터공학부 다전공 선발 안내</a></h3>  </div>
  <div class="views-field views-field-body">        <div class="field-content">학교본부에서 다전공생 학적 반영 (8/31(금) 예상) <br />
같은 날, 부전공생 합격자 확인 가능</div>  </div>  </div>
  <div class="views-row views-row-2 views-row-even views-row-last">

  <div class="views-field views-field-field-main-title">        <h3 class="field-content"><a href="/node/32701">2018년 2학기 초안지 관련 안내</a></h3>  </div>
  <div class="views-field views-field-body">        <div class="field-content">(8.28 업데이트) 컴퓨터공학부 개설 교과목 초안지 안내</div>  </div>  </div>
    </div>






</div>  </div>

</div><!-- /.block -->
<div id="block-views-news-block" class="block block-views even">

        <h2 class="block-title">새소식</h2>

  <div class="content">
    <div class="view view-news view-id-news view-display-id-block view-dom-id-852480988bcab3931bc509a48a520679">



      <div class="view-content">
        <div class="views-row views-row-1 views-row-odd views-row-first">

  <span class="views-field views-field-field-news-date">        <span class="field-content"><span class="date-display-single">8/29 (수)</span></span>  </span>
  <span class="views-field views-field-title">        <span class="field-content"><a href="/node/33185">2018년 8월 우수학위논문상 수상자 안내</a></span>  </span>  </div>
  <div class="views-row views-row-2 views-row-even">

  <span class="views-field views-field-field-news-date">        <span class="field-content"><span class="date-display-single">6/22 (금)</span></span>  </span>
  <span class="views-field views-field-title">        <span class="field-content"><a href="/node/32239">송현오 교수 연구진, 빠르고 정확한 데이터 검색을 위한 deep binary representation learning 알고리즘 고안</a></span>  </span>  </div>
  <div class="views-row views-row-3 views-row-odd">

  <span class="views-field views-field-field-news-date">        <span class="field-content"><span class="date-display-single">6/18 (월)</span></span>  </span>
  <span class="views-field views-field-title">        <span class="field-content"><a href="/node/32702">하순회 교수 연구진, LPIRC 2018에서 우수한 성적 거둬</a></span>  </span>  </div>
  <div class="views-row views-row-4 views-row-even">

  <span class="views-field views-field-field-news-date">        <span class="field-content"><span class="date-display-single">6/5 (화)</span></span>  </span>
  <span class="views-field views-field-title">        <span class="field-content"><a href="/node/32178">바이오지능연구실 SnuBiVtt, AI 국제대회에서 1등상 수상</a></span>  </span>  </div>
  <div class="views-row views-row-5 views-row-odd">

  <span class="views-field views-field-field-news-date">        <span class="field-content"><span class="date-display-single">5/31 (목)</span></span>  </span>
  <span class="views-field views-field-title">        <span class="field-content"><a href="/node/32041">이제희교수 연구진, POSNA에서 &#039;기초 논문 본상&#039; 수상</a></span>  </span>  </div>
  <div class="views-row views-row-6 views-row-even views-row-last">

  <span class="views-field views-field-field-news-date">        <span class="field-content"><span class="date-display-single">5/23 (수)</span></span>  </span>
  <span class="views-field views-field-title">        <span class="field-content"><a href="/node/32021">컴퓨터과학의 원천 아이디어가 나오기까지</a></span>  </span>  </div>
    </div>




<div class="more-link">
  <a href="/news">
    더 보기  </a>
</div>


      <div class="feed-icon">
      <a href="https://cse.snu.ac.kr/news.xml" class="feed-icon" title="새소식 구독하기"><img src="https://cse.snu.ac.kr/misc/feed.png" width="16" height="16" alt="새소식 구독하기" /></a>    </div>

</div>  </div>

</div><!-- /.block -->
<div id="block-views-notices-block-2" class="block block-views last odd">

        <h2 class="block-title">공지사항</h2>

  <div class="content">
    <div class="view view-notices view-id-notices view-display-id-block_2 view-dom-id-26c206dcc83999e526115087ab6a9bbd">



      <div class="view-content">
        <div class="views-row views-row-1 views-row-odd views-row-first">

  <span class="views-field views-field-created">        <span class="field-content">8/29 (수)</span>  </span>
  <span class="views-field views-field-title">        <span class="field-content"><a href="/node/33181">2018년 애경산업 하반기 신입수시채용</a></span>  </span>  </div>
  <div class="views-row views-row-2 views-row-even">

  <span class="views-field views-field-created">        <span class="field-content">8/29 (수)</span>  </span>
  <span class="views-field views-field-title">        <span class="field-content"><a href="/node/33179">[LG화학] 2018 하반기 채용(신입/인턴/연구원/산학) </a></span>  </span>  </div>
  <div class="views-row views-row-3 views-row-odd">

  <span class="views-field views-field-created">        <span class="field-content">8/29 (수)</span>  </span>
  <span class="views-field views-field-title">        <span class="field-content"><a href="/node/33178">2018 한화토탈 런치설명회 및 신입사원 채용</a></span>  </span>  </div>
  <div class="views-row views-row-4 views-row-even">

  <span class="views-field views-field-created">        <span class="field-content">8/29 (수)</span>  </span>
  <span class="views-field views-field-title">        <span class="field-content"><a href="/node/33177">현대자동차그룹 2018 하반기 연구장학생&amp;계약학과 모집 설명회 안내 (~9.12/수)</a></span>  </span>  </div>
  <div class="views-row views-row-5 views-row-odd">

  <span class="views-field views-field-created">        <span class="field-content">8/29 (수)</span>  </span>
  <span class="views-field views-field-title">        <span class="field-content"><a href="/node/33176">[한화시스템/시스템]  2018년 하반기 신입사원 모집</a></span>  </span>  </div>
  <div class="views-row views-row-6 views-row-even views-row-last">

  <span class="views-field views-field-created">        <span class="field-content">8/29 (수)</span>  </span>
  <span class="views-field views-field-title">        <span class="field-content"><a href="/node/33175">[삼성전기] 2018 하반기 삼성전기 신입사원 채용 및 채용상담/설명회 </a></span>  </span>  </div>
    </div>




<div class="more-link">
  <a href="/department-notices">
    더 보기  </a>
</div>


      <div class="feed-icon">
      <a href="https://cse.snu.ac.kr/department-notices.xml" class="feed-icon" title="공지사항 구독하기"><img src="https://cse.snu.ac.kr/misc/feed.png" width="16" height="16" alt="공지사항 구독하기" /></a>    </div>

</div>  </div>

</div><!-- /.block -->
  </div><!-- /.region -->
	</div></div><!-- /.section, /#top-user-regions -->
                    <div id="bottom-user-regions"><div class="section clearfix2">
          <div class="region region-user5">
    <div id="block-menu-menu-shortcuts-1" class="block block-menu first odd">


  <div class="content">
    <ul class="menu"><li class="first leaf"><a href="/about" title="">학부 소개</a></li>
<li class="leaf"><a href="https://cse.snu.ac.kr/news" title="">새소식&amp;세미나</a></li>
<li class="leaf"><a href="/directions" title="">찾아오는 길</a></li>
<li class="leaf"><a href="http://bkcse.snu.ac.kr" title="">컴퓨터미래인재양성사업단</a></li>
<li class="last leaf"><a href="/distinguished-lecture-series" title="">Distinguished Lecture Series</a></li>
</ul>  </div>

</div><!-- /.block -->
<div id="block-menu-menu-shortcuts" class="block block-menu even">


  <div class="content">
    <ul class="menu"><li class="first leaf"><a href="/people/faculty" title="">교수진</a></li>
<li class="leaf"><a href="/research/labs" title="">연구실 목록</a></li>
<li class="leaf"><a href="/node/29041" title="">Top Conference List</a></li>
<li class="leaf"><a href="http://cse.snu.ac.kr/scsc" title="">서울대학교-SCSC</a></li>
<li class="last leaf"><a href="/online-services" title="">온라인서비스(시설예약)</a></li>
</ul>  </div>

</div><!-- /.block -->
<div id="block-menu-menu-related-sites" class="block block-menu last odd">


  <div class="content">
    <ul class="menu"><li class="first leaf"><a href="http://cse.snu.ac.kr/node/24354" title="">전기·전자·컴퓨터 분야 미래 7대 기술</a></li>
<li class="leaf"><a href="http://my.snu.ac.kr/" title="">서울대학교 포털</a></li>
<li class="leaf"><a href="http://ict.snu.ac.kr/" title="">컴퓨터연구소</a></li>
<li class="leaf"><a href="http://haedong.snu.ac.kr/" title="">해동학술정보실</a></li>
<li class="last leaf"><a href="http://www.snucom.org/" title="">컴퓨터공학 동문회</a></li>
</ul>  </div>

</div><!-- /.block -->
  </div><!-- /.region -->
      </div></div><!-- /.section, /#bottom-user-regions -->
      </div></div><!-- /.section, /#main -->

      <div id="footer"><div class="section clearfix2">
        <div class="region region-footer">
    <div id="block-menu-menu-header-links" class="block block-menu first last odd">


  <div class="content">
    <ul class="menu"><li class="first leaf"><a href="http://www.snu.ac.kr/videos/2013_information_kr" title="">서울대학교</a></li>
<li class="leaf"><a href="http://eng.snu.ac.kr/" title="">공과대학</a></li>
<li class="leaf"><a href="/contact-us" title="">학부 연락처</a></li>
<li class="last leaf"><a href="https://id.snucse.org/Privacy.aspx" title="">개인정보처리방침</a></li>
</ul>  </div>

</div><!-- /.block -->
  </div><!-- /.region -->
    </div></div><!-- /.section, /#footer -->

</div></div><!-- /#page, /#page-wrapper -->

    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.5.2/jquery.min.js"></script>
<script type="text/javascript">
<!--//--><![CDATA[//><!--
window.jQuery || document.write("<script src='/sites/all/modules/jquery_update/replace/jquery/jquery.min.js'>\x3C/script>")
//--><!]]>
</script>
<script type="text/javascript" src="https://cse.snu.ac.kr/sites/default/files/js/js_4rPwjcsA1hzlHx2nz9_sLU0PwvjYpTcC3zy11uUsKH4.js"></script>
<script type="text/javascript" src="https://cse.snu.ac.kr/sites/default/files/js/js_xuinIFNSa1qR5QVYdfECh4nhg78Y0mBtL2jPUY2Bjus.js"></script>
<script type="text/javascript" src="https://cse.snu.ac.kr/sites/default/files/js/js_gBoSdTsbO5TTeOmqEi5o8yZugwRoJUJi0t2MCEMdSqk.js"></script>
<script type="text/javascript" src="https://cse.snu.ac.kr/sites/default/files/js/js_aGsdWG5NznhxYN2HxGSW9A1JUrsyIpuVE3LOW-lWdm0.js"></script>
<script type="text/javascript">
<!--//--><![CDATA[//><!--
jQuery(function(){
jQuery('#superfish-1').superfish({
delay: 400,
animation: {opacity:'show'},
speed: 'fast',
autoArrows: false,
dropShadows: false});
});
//--><!]]>
</script>
<script type="text/javascript" src="https://cse.snu.ac.kr/sites/default/files/js/js_wqN9ylV8A8MO4fAICmAnIUJKaMVxzaj07YH7ZRbd3VM.js"></script>
<script type="text/javascript">
<!--//--><![CDATA[//><!--
jQuery.extend(Drupal.settings, {"basePath":"\/","pathPrefix":"","ajaxPageState":{"theme":"dcse","theme_token":"gHohxVIvLsFkbG3ZQS_nHN3QJcZ75LWMAr9_WJrtwC8","js":{"https:\/\/ajax.googleapis.com\/ajax\/libs\/jquery\/1.5.2\/jquery.min.js":1,"0":1,"misc\/jquery.once.js":1,"misc\/drupal.js":1,"sites\/all\/modules\/jquery_update\/replace\/ui\/external\/jquery.cookie.js":1,"sites\/all\/modules\/jquery_update\/replace\/misc\/jquery.form.js":1,"misc\/ajax.js":1,"sites\/all\/modules\/spamspan\/spamspan.js":1,"public:\/\/languages\/ko_eoHOJj-35GVRvJqNV5OzTe7aMjm0xYzLgnMVWT_Co6o.js":1,"sites\/all\/modules\/lightbox2\/js\/lightbox.js":1,"sites\/all\/libraries\/superfish\/jquery.hoverIntent.minified.js":1,"sites\/all\/libraries\/superfish\/jquery.bgiframe.min.js":1,"sites\/all\/libraries\/superfish\/superfish.js":1,"sites\/all\/libraries\/superfish\/supersubs.js":1,"sites\/all\/libraries\/superfish\/supposition.js":1,"sites\/all\/libraries\/superfish\/sftouchscreen.js":1,"sites\/all\/modules\/views_slideshow\/js\/views_slideshow.js":1,"sites\/all\/libraries\/jquery.cycle\/jquery.cycle.all.js":1,"sites\/all\/modules\/views_slideshow\/contrib\/views_slideshow_cycle\/js\/views_slideshow_cycle.js":1,"sites\/all\/modules\/views\/js\/base.js":1,"misc\/progress.js":1,"sites\/all\/modules\/views\/js\/ajax_view.js":1,"1":1,"sites\/all\/themes\/dcse\/js\/jquery.cookie.js":1,"sites\/all\/themes\/dcse\/js\/script.js":1},"css":{"modules\/system\/system.base.css":1,"modules\/system\/system.messages.css":1,"sites\/all\/modules\/date\/date_api\/date.css":1,"sites\/all\/modules\/date\/date_popup\/themes\/datepicker.1.7.css":1,"modules\/field\/theme\/field.css":1,"modules\/node\/node.css":1,"modules\/search\/search.css":1,"modules\/user\/user.css":1,"sites\/all\/modules\/views\/css\/views.css":1,"sites\/all\/modules\/ctools\/css\/ctools.css":1,"sites\/all\/modules\/lightbox2\/css\/lightbox.css":1,"sites\/all\/libraries\/superfish\/css\/superfish.css":1,"sites\/all\/libraries\/superfish\/css\/superfish-vertical.css":1,"sites\/all\/libraries\/superfish\/css\/superfish-navbar.css":1,"sites\/all\/modules\/views_slideshow\/views_slideshow.css":1,"modules\/locale\/locale.css":1,"sites\/all\/modules\/views_slideshow\/views_slideshow_controls_text.css":1,"sites\/all\/modules\/views_slideshow\/contrib\/views_slideshow_cycle\/views_slideshow_cycle.css":1,"sites\/all\/themes\/dcse\/css\/contents.scss":1,"sites\/all\/themes\/dcse\/css\/forms.scss":1,"sites\/all\/themes\/dcse\/css\/structures.scss":1,"sites\/all\/themes\/dcse\/css\/print.scss":1,"sites\/all\/themes\/dcse\/css\/ie\/ie8.css":1}},"lightbox2":{"rtl":"0","file_path":"\/(\\w\\w\/)public:\/","default_image":"\/sites\/all\/modules\/lightbox2\/images\/brokenimage.jpg","border_size":10,"font_color":"000","box_color":"fff","top_position":"","overlay_opacity":"0.8","overlay_color":"000","disable_close_click":1,"resize_sequence":0,"resize_speed":400,"fade_in_speed":400,"slide_down_speed":600,"use_alt_layout":0,"disable_resize":0,"disable_zoom":0,"force_show_nav":0,"show_caption":1,"loop_items":0,"node_link_text":"View Image Details","node_link_target":0,"image_count":"Image !current of !total","video_count":"Video !current of !total","page_count":"Page !current of !total","lite_press_x_close":"press \u003Ca href=\u0022#\u0022 onclick=\u0022hideLightbox(); return FALSE;\u0022\u003E\u003Ckbd\u003Ex\u003C\/kbd\u003E\u003C\/a\u003E to close","download_link_text":"","enable_login":false,"enable_contact":false,"keys_close":"c x 27","keys_previous":"p 37","keys_next":"n 39","keys_zoom":"z","keys_play_pause":"32","display_image_size":"original","image_node_sizes":"()","trigger_lightbox_classes":"","trigger_lightbox_group_classes":"","trigger_slideshow_classes":"","trigger_lightframe_classes":"","trigger_lightframe_group_classes":"","custom_class_handler":0,"custom_trigger_classes":"","disable_for_gallery_lists":true,"disable_for_acidfree_gallery_lists":true,"enable_acidfree_videos":true,"slideshow_interval":5000,"slideshow_automatic_start":true,"slideshow_automatic_exit":true,"show_play_pause":true,"pause_on_next_click":false,"pause_on_previous_click":true,"loop_slides":false,"iframe_width":600,"iframe_height":400,"iframe_border":1,"enable_video":0},"viewsSlideshow":{"slideshow-slideshow":{"methods":{"goToSlide":["viewsSlideshowPager","viewsSlideshowSlideCounter","viewsSlideshowCycle"],"nextSlide":["viewsSlideshowPager","viewsSlideshowSlideCounter","viewsSlideshowCycle"],"pause":["viewsSlideshowControls","viewsSlideshowCycle"],"play":["viewsSlideshowControls","viewsSlideshowCycle"],"previousSlide":["viewsSlideshowPager","viewsSlideshowSlideCounter","viewsSlideshowCycle"],"transitionBegin":["viewsSlideshowPager","viewsSlideshowSlideCounter"],"transitionEnd":[]},"paused":0}},"viewsSlideshowControls":{"slideshow-slideshow":{"bottom":{"type":"viewsSlideshowControlsText"}}},"viewsSlideshowCycle":{"#views_slideshow_cycle_main_slideshow-slideshow":{"num_divs":12,"id_prefix":"#views_slideshow_cycle_main_","div_prefix":"#views_slideshow_cycle_div_","vss_id":"slideshow-slideshow","effect":"fade","transition_advanced":1,"timeout":5000,"speed":500,"delay":0,"sync":1,"random":0,"pause":1,"pause_on_click":0,"action_advanced":1,"start_paused":0,"remember_slide":0,"remember_slide_days":1,"pause_when_hidden":0,"pause_when_hidden_type":"full","amount_allowed_visible":"","nowrap":0,"fixed_height":0,"items_per_slide":4,"wait_for_image_load":1,"wait_for_image_load_timeout":3000,"cleartype":0,"cleartypenobg":0,"advanced_options":"{}"}},"views":{"ajax_path":"\/views\/ajax","ajaxViews":{"views_dom_id:0de5f9eb56a2d2646719ae31d4eafae6":{"view_name":"slideshow","view_display_id":"slideshow","view_args":"","view_path":"home","view_base_path":"manage-slideshow","view_dom_id":"0de5f9eb56a2d2646719ae31d4eafae6","pager_element":0}}},"dcse":{"langcode":"ko","dropdown_menu_sidebar":"no"}});
//--><!]]>
</script>
      </body>
</html>
'''


class MyHtml(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start : ', tag)

    def handle_endtag(self, tag):
        print('End : ', tag)

    def handle_data(self, data):
        print('Data : ', data)


if __name__ == '__main__':
    # par = MyHtml()
    # par.feed('<HTML>test</HTML>')

    soup = BeautifulSoup(html_doc, 'html.parser')
    soup.name
