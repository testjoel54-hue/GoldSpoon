#!/usr/bin/env python3
"""Regenerate the bilingual HTML pages. The output in site/ is also directly editable."""
from pathlib import Path
from html import escape
import json
ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'site'
PHONE='(469) 900-8187'
TEL='tel:+14699008187'
ADDRESS='3040 Old Denton Rd, Carrollton, TX 75007'
MAP='https://www.google.com/maps/search/?api=1&query=Gold+Spoon+3040+Old+Denton+Rd+Carrollton+TX+75007'
YELP='https://www.yelp.com/biz/gold-spoon-carrollton'
DELIVERY='https://www.ubereats.com/store/gold-spoon/l_DAAALMWHWkSzIe1ppxzw'
I='/assets/img/'

L={
 'en':{
  'nav':{'home':'Home','menu':'Menu','story':'Our Space','order':'Order','visit':'Visit'},
  'call':'Call us','hero-kicker':'WELCOME TO GOLD SPOON · CARROLLTON, TX',
  'hero-title':'Korean comfort,<br><em>beautifully shared.</em>',
  'hero-hangul':'한식의 따뜻함을 담다',
  'hero-lead':'Rich flavors. Comforting classics. Good company. Discover the warmth of Korean cooking at Gold Spoon, right here in Carrollton.',
  'see-menu':'Explore the menu','visit-us':'Plan your visit','gallery-note':'AN ILLUSTRATED VIEW OF OUR STORE',
  'hero-location':'CARROLLTON · TEXAS','info-location':'Find us','info-location-body':'3040 Old Denton Rd<br>Carrollton, TX 75007',
  'info-hours':'Come hungry','info-hours-body':'Lunch &amp; dinner, 7 days a week',
  'info-call':'Say hello','info-call-body':PHONE,
  'story-kicker':'A PLACE TO GATHER','story-title':'A warm welcome.<br><em>A full table.</em>',
  'story-hangul':'맛있는 음식, 좋은 사람들',
  'story-body':'From simmering stews to generous shared dishes, Korean food is about the joy of gathering. Gold Spoon pairs familiar flavors with a relaxed, welcoming dining room.',
  'story-button':'Discover our space','story-photo-label':'INTERIOR ILLUSTRATION',
  'dishes-kicker':'FROM OUR TABLE','dishes-title':'The favorites worth gathering for.',
  'dishes-sub':'A few Korean classics frequently highlighted by guests. Visit our menu page for more dishes and Korean names.',
  'dishes-all':'Browse more dishes',
  'quote':'Come for the flavors. <em>Stay for the feeling.</em>', 'quote-button':'Find your way here',
  'visit-kicker':'GOOD FOOD, GOOD COMPANY','visit-title':'There’s a place<br>for you here.',
  'visit-body':'Stop by for lunch, settle in for dinner, or call ahead with a question. We’re in Carrollton’s NorthCrest Village area.',
  'address-label':'Find us at','visit-button':'Directions to Gold Spoon','hours-kicker':'WHEN TO VISIT','hours-title':'Opening hours',
  'hours-note':'Hours may change on holidays. Please call before visiting.',
  'footer-about':'Korean comfort food, warming soups, shareable dishes, and a welcoming table in Carrollton, Texas.',
  'footer-links':'Explore','footer-contact':'Get in touch','footer-find':'Find us','footer-review':'See more on Yelp',
  'footer-fine':'An original illustrated concept website for Gold Spoon.','footer-language':'English · 한국어',
  'menu-kicker':'THE FOOD · 음식','menu-title':'Made to <em>share.</em>','menu-desc':'A curated guide to the Korean dishes guests mention and enjoy. Select a category or search in English or Korean.',
  'search-label':'Search the menu','search-placeholder':'Search bulgogi, soup, 갈비...',
  'category-all':'All dishes','menu-no-results':'No dishes matched your search. Try another name or category.',
  'menu-note':'This is a curated selection of dishes identified from restaurant listings and reviews, not a confirmed current price list. Dish availability and prices may change. Please call for the latest menu and pricing.',
  'story-page-kicker':'THE PLACE · 공간','story-page-title':'Come in. <em>Stay awhile.</em>',
  'story-page-desc':'Explore the warmth of Gold Spoon through original, stylized visuals inspired by the storefront and dining-room references.',
  'story-page-intro-kicker':'WELCOME INSIDE','story-page-intro-title':'Korean flavor.<br>Room to <em>gather.</em>',
  'story-page-intro-body':'A comfortable place to catch up over a bowl of soup, share a plate of bulgogi, or discover a new favorite. The atmosphere is simple: warm light, an inviting table, and Korean dishes made for company.',
  'gallery-kicker':'A CLOSER LOOK','gallery-title':'The space & the details','gallery-sub':'These are original illustrations inspired by supplied photographs, not documentary photos or an exact reconstruction.',
  'gallery-exterior':'Illustrated storefront','gallery-interior':'Illustrated dining room','gallery-logo':'Gold Spoon emblem',
  'gallery-yelp':'See guest photos on Yelp','gallery-tip':'Tap an image to take a closer look.',
  'order-kicker':'ORDER YOUR WAY','order-title':'Craving <em>Korean?</em>',
  'order-desc':'Prefer eating at home? Choose pickup by phone, or check current third-party delivery availability.',
  'order-intro-kicker':'TAKE IT TO GO','order-intro-title':'Your favorites, your way.',
  'order-intro-body':'Start with a call for a pickup request or open the restaurant’s delivery listing. Availability, service fees, and menus may differ by platform.',
  'pickup-title':'Pickup by phone','pickup-body':'Call Gold Spoon to ask about the current menu, place a pickup request, and confirm when your order will be ready.',
  'pickup-button':'Call for pickup','delivery-title':'Home delivery','delivery-body':'View the Gold Spoon listing on Uber Eats to check delivery coverage, available dishes, pricing, and checkout options.',
  'delivery-button':'View on Uber Eats','order-note':'Online checkout is provided by a third party, not this website. Please confirm opening hours and delivery coverage with the provider.',
  'visit-page-kicker':'FIND US · 오시는 길','visit-page-title':'Your seat <em>awaits.</em>',
  'visit-page-desc':'Easy to find in Carrollton, close to the heart of the local Korean dining scene. We look forward to welcoming you.',
  'visit-contact-title':'Come on in.','visit-address-label':'Restaurant address','visit-phone-label':'Call the restaurant',
  'visit-hours-label':'Restaurant hours','visit-map-button':'Get directions','visit-map-caption':'3040 Old Denton Rd · Carrollton, Texas',
  'visit-map-note':'Open directions in Google Maps','visit-hours-note':'Holiday and special-event hours may differ. Please call ahead.',
  'weekdays':['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],
 },
 'ko':{
  'nav':{'home':'홈','menu':'메뉴','story':'매장 소개','order':'주문 안내','visit':'오시는 길'},
  'call':'전화 문의','hero-kicker':'금수저 · 텍사스 캐롤턴',
  'hero-title':'정성을 담은 한식,<br><em>따뜻한 한 끼.</em>',
  'hero-hangul':'한국의 맛과 온기를 전합니다',
  'hero-lead':'깊은 맛의 국물 요리부터 함께 나누기 좋은 한식까지. 캐롤턴 금수저에서 편안하고 따뜻한 식사 시간을 즐겨보세요.',
  'see-menu':'메뉴 살펴보기','visit-us':'방문 안내','gallery-note':'일러스트로 표현한 매장 외관',
  'hero-location':'캐롤턴 · 텍사스','info-location':'매장 위치','info-location-body':'3040 Old Denton Rd<br>Carrollton, TX 75007',
  'info-hours':'영업 안내','info-hours-body':'연중 매일 점심 · 저녁 영업',
  'info-call':'전화 문의','info-call-body':PHONE,
  'story-kicker':'함께하는 한 끼','story-title':'반가운 인사와<br><em>따뜻한 식탁.</em>',
  'story-hangul':'맛있는 음식, 좋은 사람들',
  'story-body':'보글보글 끓는 찌개부터 여럿이 함께 즐기는 요리까지. 한식의 즐거움은 좋은 사람들과 식탁을 나누는 데 있습니다. 금수저에서 편안하고 즐거운 시간을 보내세요.',
  'story-button':'매장 둘러보기','story-photo-label':'매장 내부 일러스트',
  'dishes-kicker':'금수저의 인기 메뉴','dishes-title':'함께 나누고 싶은 한식.',
  'dishes-sub':'방문객들에게 사랑받는 대표 메뉴를 소개합니다. 더 많은 음식은 메뉴 페이지에서 확인하세요.',
  'dishes-all':'메뉴 전체 보기',
  'quote':'맛있는 음식과 <em>기분 좋은 만남.</em>','quote-button':'오시는 길 보기',
  'visit-kicker':'반가운 만남','visit-title':'금수저에서<br>만나요.',
  'visit-body':'점심 식사, 저녁 모임, 메뉴 문의까지 언제든 연락해 주세요. 매장은 캐롤턴 노스크레스트 빌리지 인근에 있습니다.',
  'address-label':'매장 주소','visit-button':'길찾기','hours-kicker':'방문 가능 시간','hours-title':'영업시간',
  'hours-note':'공휴일에는 영업시간이 달라질 수 있으니 방문 전 전화로 확인해 주세요.',
  'footer-about':'캐롤턴에서 따뜻한 국물 요리와 다양한 한식을 함께 나눌 수 있는 금수저입니다.',
  'footer-links':'둘러보기','footer-contact':'연락처','footer-find':'매장 위치','footer-review':'Yelp 리뷰 보기',
  'footer-fine':'금수저를 위한 오리지널 일러스트 기반 웹사이트 시안입니다.','footer-language':'English · 한국어',
  'menu-kicker':'금수저의 음식 · MENU','menu-title':'함께 나누는 <em>한식.</em>','menu-desc':'리뷰와 식당 소개에서 확인할 수 있는 메뉴를 모았습니다. 종류를 선택하거나 한글·영문으로 검색해 보세요.',
  'search-label':'메뉴 검색','search-placeholder':'불고기, 갈비, soup 검색',
  'category-all':'전체 메뉴','menu-no-results':'검색된 메뉴가 없습니다. 다른 단어나 분류를 선택해 주세요.',
  'menu-note':'식당 소개 및 리뷰에서 확인된 대표 메뉴를 정리한 안내 페이지이며, 현재 공식 메뉴판이나 가격표를 의미하지 않습니다. 가격과 제공 여부는 매장에 문의해 주세요.',
  'story-page-kicker':'금수저 공간 소개','story-page-title':'편안하게 오셔서 <em>즐겨보세요.</em>',
  'story-page-desc':'매장 외관과 내부 사진을 바탕으로 새롭게 제작한 일러스트를 통해 금수저의 분위기를 만나보세요.',
  'story-page-intro-kicker':'어서 오세요','story-page-intro-title':'한국의 맛,<br>함께하는 <em>공간.</em>',
  'story-page-intro-body':'따끈한 국물 한 그릇을 즐기거나 불고기를 함께 나누며 이야기꽃을 피우기 좋은 곳. 따뜻한 조명 아래 여유로운 식사를 즐겨보세요.',
  'gallery-kicker':'매장 이미지','gallery-title':'공간과 디테일','gallery-sub':'제공된 사진을 참고해 새롭게 제작한 일러스트이며 실제 모습과 완전히 동일한 사진은 아닙니다.',
  'gallery-exterior':'매장 외관 일러스트','gallery-interior':'식사 공간 일러스트','gallery-logo':'금수저 로고',
  'gallery-yelp':'Yelp에서 실제 사진 보기','gallery-tip':'이미지를 누르면 크게 볼 수 있습니다.',
  'order-kicker':'주문 안내','order-title':'한식이 <em>생각날 때.</em>',
  'order-desc':'매장에 전화하여 포장 주문을 문의하거나 외부 배달 플랫폼의 현재 이용 가능 여부를 확인해 보세요.',
  'order-intro-kicker':'집에서도 금수저','order-intro-title':'원하는 방식으로 즐기세요.',
  'order-intro-body':'전화로 포장 주문을 문의하거나 배달 서비스 페이지를 확인해 주세요. 메뉴 및 수수료는 플랫폼에 따라 달라질 수 있습니다.',
  'pickup-title':'전화 포장 주문','pickup-body':'금수저에 전화해 오늘의 메뉴, 포장 가능 여부, 주문 준비 시간을 문의하세요.',
  'pickup-button':'포장 문의 전화','delivery-title':'배달 서비스','delivery-body':'Uber Eats 금수저 페이지에서 배달 가능 지역, 메뉴, 가격, 결제 정보를 확인할 수 있습니다.',
  'delivery-button':'Uber Eats에서 확인','order-note':'온라인 결제는 이 웹사이트가 아닌 외부 서비스에서 진행됩니다. 이용 가능 지역과 운영 시간을 확인해 주세요.',
  'visit-page-kicker':'금수저 오시는 길','visit-page-title':'금수저에서 <em>만나요.</em>',
  'visit-page-desc':'캐롤턴 한인 식당가 인근에 위치한 금수저. 맛있는 한식과 함께 여러분을 기다립니다.',
  'visit-contact-title':'방문 안내','visit-address-label':'매장 주소','visit-phone-label':'전화번호',
  'visit-hours-label':'영업시간','visit-map-button':'길찾기','visit-map-caption':'3040 Old Denton Rd · Carrollton, Texas',
  'visit-map-note':'Google 지도에서 길찾기','visit-hours-note':'공휴일 및 특별 일정에는 영업시간이 다를 수 있으니 전화로 확인해 주세요.',
  'weekdays':['월요일','화요일','수요일','목요일','금요일','토요일','일요일'],
 }
}

CATEGORIES=[('soups','Soups & Stews','국물 · 찌개'),('grill','Grilled & Sizzling','구이 · 볶음'),('shared','To Share','함께 나누는 요리'),('comfort','Comfort Classics','분식 · 별미')]
MENU=[
 ('soups','Army Stew','부대찌개','A warming Korean hot pot favorite with bold, savory flavors.','푸짐하고 깊은 맛을 즐기는 한국식 전골.'),
 ('soups','Short Rib Soup','갈비탕','Rich beef broth with tender short ribs.','갈비의 깊은 맛이 우러난 따뜻한 국물 요리.'),
 ('soups','Spicy Beef Soup','매운 소고기탕','Hearty beef soup with a pleasantly spicy finish.','얼큰한 국물과 소고기가 어우러진 메뉴.'),
 ('soups','Rice Cake & Dumpling Soup','떡만둣국','Soft rice cakes and dumplings in a comforting broth.','떡과 만두가 들어간 정겨운 국물 요리.'),
 ('soups','Gamjatang','감자탕','A traditional pork bone soup, rich and satisfying.','진하고 푸짐한 돼지 등뼈 국물 요리.'),
 ('soups','Bulgogi Mushroom Hot Pot','불고기 버섯전골','Bulgogi and mushrooms served in a savory hot pot.','불고기와 버섯이 어우러진 전골 요리.'),
 ('soups','Seafood Soup','해물탕','A Korean seafood soup with depth and warmth.','해산물의 풍미를 담은 따뜻한 탕.'),
 ('soups','Beef Intestine Soup','곱창국물요리','A rich Korean soup favorite for hearty tastes.','깊고 진한 풍미의 국물 요리.'),
 ('soups','Soft Seafood Tofu Soup','해물 순두부찌개','A bubbling soft tofu dish with seafood.','부드러운 순두부와 해산물이 어우러진 찌개.'),
 ('grill','Beef Bulgogi','소불고기','Tender beef with sweet and savory Korean seasoning.','달콤짭짤한 양념으로 즐기는 소고기 요리.'),
 ('grill','Spicy Pork Bulgogi','제육불고기','Seasoned pork with a spicy, satisfying kick.','매콤한 양념이 매력적인 돼지고기 요리.'),
 ('grill','LA Galbi','LA 갈비','Korean-style marinated short ribs.','양념을 입혀 구워낸 한국식 갈비.'),
 ('grill','Stir-Fried Brisket','차돌박이 볶음','Savory stir-fried beef brisket.','차돌박이의 고소한 맛을 살린 볶음 요리.'),
 ('grill','Spicy Stir-Fried Squid','오징어볶음','Squid stir-fried with lively Korean seasoning.','매콤하고 쫄깃한 오징어 요리.'),
 ('grill','Pork Cutlet','돈까스','A crispy, golden comfort-food favorite.','바삭하게 튀긴 인기 메뉴.'),
 ('shared','Boiled Pork Belly / Bossam','보쌈','Tender pork served for wrapping and sharing.','부드러운 수육을 함께 즐기는 대표 메뉴.'),
 ('shared','Jokbal','족발','A traditional Korean braised pork favorite.','쫄깃한 식감과 진한 풍미의 족발.'),
 ('shared','Seafood Scallion Pancake','해물파전','A savory, crisp-edged scallion and seafood pancake.','해물과 파를 넣어 부친 바삭한 전.'),
 ('shared','Homemade Dumplings','수제만두','Dumplings featured among popular diner favorites.','손맛이 느껴지는 만두 메뉴.'),
 ('comfort','Tteokbokki','떡볶이','Chewy rice cakes with spicy-sweet seasoning.','쫄깃하고 매콤달콤한 떡볶이.'),
 ('comfort','Fish Cake','어묵','A familiar Korean comfort favorite.','부담 없이 즐기기 좋은 어묵.'),
 ('comfort','Ramen','라면','Hot, comforting noodles with classic Korean flavor.','따뜻하고 얼큰하게 즐기는 라면.'),
 ('comfort','Kimchi Fried Rice','김치볶음밥','Fried rice with vibrant kimchi flavor.','김치의 풍미가 살아 있는 볶음밥.'),
]
DISHES=[('bossam','Boiled Pork Belly','보쌈','For the table, and for good company.','좋은 사람들과 나누기 좋은 한 접시.'),('stew','Hearty Stews','부대찌개','Warm, comforting, and full of flavor.','뜨끈한 국물에 담긴 깊은 맛.'),('pancake','Seafood Pancake','해물파전','Golden, savory, made to share.','고소하고 바삭한 별미.')]

# Semantic helpers.
def ex(s):return escape(str(s),quote=True)
def route(lang,page):
    p='' if page=='home' else page+'/'
    return ('/ko/' if lang=='ko' else '/')+p

def navbar(lang,page):
    t=L[lang]; names=t['nav']
    en=route('en',page);ko=route('ko',page)
    links=''.join(f'<a href="{route(lang,p)}"'+(' aria-current="page"' if page==p else '')+f'>{names[p]}</a>' for p in ('home','menu','story','order','visit'))
    return f'''<div class="topline"><div class="container topline-inner"><span>GOLD SPOON <b>금수저</b> · KOREAN CUISINE</span><span>{'CARROLLTON, TEXAS · LUNCH & DINNER' if lang=='en' else '텍사스 캐롤턴 · 점심과 저녁'}</span></div></div>
<header class="site-header"><div class="container header-inner">
 <a class="brand" href="{route(lang,'home')}" aria-label="Gold Spoon {names['home']}"><img class="brand-icon" src="{I}gold-spoon-emblem.webp" alt="" width="65" height="65"><span class="brand-words"><span class="brand-main">GOLD SPOON</span><span class="brand-sub">금수저 · KOREAN CUISINE</span></span></a>
 <nav class="desktop-nav" aria-label="{'Main navigation' if lang=='en' else '주 메뉴'}">{links}</nav>
 <div class="header-actions"><div class="lang-switch" aria-label="{'Select language' if lang=='en' else '언어 선택'}"><a href="{en}" lang="en" aria-label="English"{' aria-current="true"' if lang=='en' else ''}>EN</a><a href="{ko}" lang="ko" aria-label="한국어"{' aria-current="true"' if lang=='ko' else ''}>KO</a></div><a class="header-call" href="{TEL}">{t['call']} ↗</a><button class="menu-trigger" type="button" data-menu-trigger aria-expanded="false" aria-controls="mobile-navigation" aria-label="{'Open menu' if lang=='en' else '메뉴 열기'}"><span></span><span></span></button></div>
</div><nav class="mobile-nav" id="mobile-navigation" data-mobile-nav aria-label="{'Mobile navigation' if lang=='en' else '모바일 메뉴'}"><div class="container">{links}<a href="{TEL}">{t['call']}: {PHONE}</a></div></nav></header>'''

def footer(lang):
 t=L[lang]
 links=''.join(f'<a href="{route(lang,p)}">{t["nav"][p]}</a>' for p in ('home','menu','story','order','visit'))
 return f'''<footer class="site-footer"><div class="container"><div class="footer-grid"><div><a class="footer-brand" href="{route(lang,'home')}"><img src="{I}gold-spoon-emblem.webp" alt="" width="74" height="74"><span><strong>Gold Spoon</strong><small>금수저 · Korean Cuisine</small></span></a><p class="footer-about">{t['footer-about']}</p><a href="{YELP}" target="_blank" rel="noopener noreferrer" style="color:var(--gold);font-size:12px;text-decoration:underline;text-underline-offset:4px">{t['footer-review']} ↗</a></div><div><h3 class="footer-heading">{t['footer-links']}</h3><nav class="footer-links" aria-label="Footer navigation">{links}</nav></div><div><h3 class="footer-heading">{t['footer-contact']}</h3><div class="footer-links"><a href="{TEL}">{PHONE}</a><a href="{MAP}" target="_blank" rel="noopener noreferrer">{t['visit-map-button']} ↗</a><a href="{DELIVERY}" target="_blank" rel="noopener noreferrer">Uber Eats ↗</a></div></div><div><h3 class="footer-heading">{t['footer-find']}</h3><div class="footer-links"><span>3040 Old Denton Rd</span><span>Carrollton, TX 75007</span><a href="{route('ko' if lang=='en' else 'en','home')}">{'한국어로 보기' if lang=='en' else 'View in English'} ↗</a></div></div></div><div class="footer-fine"><span>© 2026 GOLD SPOON · 금수저</span><span>{t['footer-fine']}</span></div></div></footer>'''

def head(lang,page,title,description):
 schema={"@context":"https://schema.org","@type":"Restaurant","name":"Gold Spoon 금수저","servesCuisine":"Korean","telephone":"+14699008187","address":{"@type":"PostalAddress","streetAddress":"3040 Old Denton Rd","addressLocality":"Carrollton","addressRegion":"TX","postalCode":"75007","addressCountry":"US"},"sameAs":[YELP],"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday"],"opens":"11:30","closes":"15:00"},{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday"],"opens":"17:00","closes":"23:00"},{"@type":"OpeningHoursSpecification","dayOfWeek":["Friday","Saturday"],"opens":"11:30","closes":"15:00"},{"@type":"OpeningHoursSpecification","dayOfWeek":["Friday","Saturday"],"opens":"17:00","closes":"00:00"},{"@type":"OpeningHoursSpecification","dayOfWeek":"Sunday","opens":"12:00","closes":"22:00"}]}
 return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#14211d"><meta name="description" content="{ex(description)}"><title>{ex(title)}</title><meta property="og:type" content="website"><meta property="og:title" content="{ex(title)}"><meta property="og:description" content="{ex(description)}"><link rel="icon" type="image/svg+xml" href="/assets/img/favicon.svg"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=DM+Sans:wght@400;500;600;700;800&family=Noto+Sans+KR:wght@400;500;600;700;800&family=Noto+Serif+KR:wght@400;500;600;700&display=swap" rel="stylesheet"><link href="/assets/css/styles.css" rel="stylesheet"><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False,separators=(',',':'))}</script><script src="/assets/js/site.js" defer></script></head><body><a class="skip-link" href="#main">{'Skip to content' if lang=='en' else '본문으로 건너뛰기'}</a>{navbar(lang,page)}'''

def doc(lang,page,title,description,main):return head(lang,page,title,description)+f'<main id="main">{main}</main>'+footer(lang)+'</body></html>'
def btn(text,href,kind='gold',external=False):return f'<a class="btn btn-{kind}" href="{ex(href)}"'+(' target="_blank" rel="noopener noreferrer"' if external else '')+f'>{text}<span class="btn-arrow" aria-hidden="true">↗</span></a>'

def hours_rows(lang,classes):
 t=L[lang]; days=t['weekdays']; out=''
 for i,day in enumerate(days):
  value=('11:30 AM – 3 PM<br>5 PM – 11 PM' if i<4 else '11:30 AM – 3 PM<br>5 PM – 12 AM' if i<6 else '12 PM – 10 PM')
  out+=f'<div class="{classes}"><strong>{day}</strong><span>{value}</span></div>'
 return out

def home(lang):
 t=L[lang]
 cards=''
 for i,(slug,en,ko,desc,desc_ko) in enumerate(DISHES,1):
  cards+=f'''<a class="dish-card reveal" href="{route(lang,'menu')}"><img src="{I}dish-{slug}.svg" alt="{'Illustration of '+en if lang=='en' else ko+' 일러스트'}" width="720" height="620" loading="lazy"><div class="dish-card-body"><div class="dish-card-top"><span class="dish-number">FEATURE {i:02}</span><span class="dish-hangul">{ko}</span></div><h3>{en if lang=='en' else ko}</h3><p>{desc if lang=='en' else desc_ko}</p></div></a>'''
 return f'''<section class="hero"><div class="container hero-inner"><div class="hero-copy"><div class="eyebrow">{t['hero-kicker']}</div><h1{' class="hangul"' if lang=='ko' else ''}>{t['hero-title']}</h1><p class="ko-line">{t['hero-hangul']}</p><p class="lead">{t['hero-lead']}</p><div class="hero-cta">{btn(t['see-menu'],route(lang,'menu'))}{btn(t['visit-us'],route(lang,'visit'),'outline-light')}</div></div><figure class="hero-art"><img src="{I}storefront.webp" alt="{'Original illustration of the Gold Spoon restaurant storefront' if lang=='en' else '금수저 매장 외관을 참고해 제작한 일러스트'}" width="1672" height="941" fetchpriority="high"><div class="hero-seal" aria-hidden="true"><span>금<br>수저</span></div><figcaption><span>{t['gallery-note']}</span><span>{t['hero-location']}</span></figcaption></figure></div></section><div class="pattern-trim" aria-hidden="true"></div>
<section class="info-band"><div class="container info-band-inner"><div class="info-stat"><span class="symbol" aria-hidden="true">⌖</span><div><small>{t['info-location']}</small><strong>{t['info-location-body']}</strong></div></div><div class="info-stat"><span class="symbol" aria-hidden="true">◷</span><div><small>{t['info-hours']}</small><strong>{t['info-hours-body']}</strong></div></div><div class="info-stat"><span class="symbol" aria-hidden="true">✳</span><div><small>{t['info-call']}</small><strong><a href="{TEL}">{PHONE}</a></strong></div></div></div></section>
<section class="section story-preview"><div class="container story-preview-grid"><div class="image-frame reveal"><img src="{I}interior.webp" alt="{'Stylized illustration of the Gold Spoon dining room' if lang=='en' else '금수저 식사 공간 일러스트'}" loading="lazy" width="1448" height="1086"><span class="photo-label">{t['story-photo-label']}</span></div><div class="story-copy reveal"><div class="eyebrow">{t['story-kicker']}</div><h2{' class="hangul"' if lang=='ko' else ''}>{t['story-title']}</h2><div class="korean-mark">{t['story-hangul']}</div><p>{t['story-body']}</p>{btn(t['story-button'],route(lang,'story'),'outline-ink')}</div></div></section>
<section class="section dishes-section"><div class="container"><div class="section-heading reveal"><div><div class="eyebrow">{t['dishes-kicker']}</div><h2{' class="hangul"' if lang=='ko' else ''}>{t['dishes-title']}</h2></div><p class="section-sub">{t['dishes-sub']}</p></div><div class="dish-grid">{cards}</div><div class="section-cta">{btn(t['dishes-all'],route(lang,'menu'),'gold')}</div></div></section>
<section class="quote-band"><div class="container quote-inner"><h2{' class="hangul"' if lang=='ko' else ''}>{t['quote']}</h2>{btn(t['quote-button'],route(lang,'visit'),'outline-light')}</div></section>
<section class="section visit-preview"><div class="container visit-preview-grid"><div class="story-copy reveal"><div class="eyebrow">{t['visit-kicker']}</div><h2{' class="hangul"' if lang=='ko' else ''}>{t['visit-title']}</h2><p>{t['visit-body']}</p><div class="address-card"><small>{t['address-label']}</small><strong>{ADDRESS}</strong></div>{btn(t['visit-button'],MAP,'ink',True)}</div><div class="hours-widget reveal"><div class="eyebrow">{t['hours-kicker']}</div><h3>{t['hours-title']}</h3>{hours_rows(lang,'hours-widget-row')}<p style="font-size:11px;line-height:1.8;color:#b7bfb2;margin-top:15px">{t['hours-note']}</p></div></div></section>'''

def page_hero(lang,page):
 t=L[lang]
 return f'''<section class="page-hero"><div class="container" style="position:relative;z-index:1"><div class="eyebrow">{t[page+'-kicker'] if page!='story' and page!='visit' else t[page+'-page-kicker']}</div><h1{' class="hangul"' if lang=='ko' else ''}>{t[page+'-title'] if page in ('menu','order') else t[page+'-page-title']}</h1><p>{t[page+'-desc'] if page in ('menu','order') else t[page+'-page-desc']}</p><nav class="breadcrumbs" aria-label="Breadcrumb"><a href="{route(lang,'home')}">{t['nav']['home']}</a><span aria-hidden="true">/</span><span>{t['nav'][page]}</span></nav></div></section><div class="pattern-trim" aria-hidden="true"></div>'''

def menu_page(lang):
 t=L[lang]
 buttons=f'<button class="active" type="button" data-filter="all" aria-pressed="true">{t["category-all"]}</button>'
 buttons+=''.join(f'<button type="button" data-filter="{cat}" aria-pressed="false">{name_en if lang=="en" else name_ko}</button>' for cat,name_en,name_ko in CATEGORIES)
 sections=''
 for i,(cat,name_en,name_ko) in enumerate(CATEGORIES,1):
  rendered=''
  for category,en,ko,desc_en,desc_ko in MENU:
   if cat!=category:continue
   rendered+=f'''<article class="menu-item" data-category="{cat}" data-menu-item="{ex(en+' '+ko+' '+desc_en+' '+desc_ko)}"><div class="menu-item-top"><h3>{ex(en if lang=='en' else ko)}</h3><span class="item-hangul">{ex(ko if lang=='en' else en)}</span></div><p>{ex(desc_en if lang=='en' else desc_ko)}</p></article>'''
  sections+=f'''<section class="menu-category" data-menu-section><div class="menu-category-header"><h2>{name_en if lang=='en' else name_ko}<span>{name_ko if lang=='en' else name_en}</span></h2><span class="category-number">0{i} / 04</span></div><div class="menu-list">{rendered}</div></section>'''
 return page_hero(lang,'menu')+f'''<section class="menu-main"><div class="container"><div class="menu-toolbar"><div class="category-buttons" role="group" aria-label="{'Filter menu categories' if lang=='en' else '메뉴 종류 선택'}">{buttons}</div><input class="menu-search" type="search" data-menu-search aria-label="{t['search-label']}" placeholder="{t['search-placeholder']}" autocomplete="off"></div><p class="menu-count" data-menu-count aria-live="polite"></p><div class="menu-empty" data-menu-empty hidden>{t['menu-no-results']}</div>{sections}<p class="menu-note">{t['menu-note']} <a href="{TEL}" style="text-decoration:underline;font-weight:700">{PHONE}</a>.</p></div></section>'''

def story_page(lang):
 t=L[lang]
 def tile(name,src,alt,cls):
  return f'''<button type="button" class="gallery-photo {cls}" data-open-image="{I}{src}" data-image-alt="{ex(alt)}" aria-label="{'Enlarge' if lang=='en' else '확대 보기'}: {ex(alt)}"><img src="{I}{src}" alt="{ex(alt)}" loading="lazy"><figcaption>{name} ↗</figcaption></button>'''
 gal=tile(t['gallery-exterior'],'storefront.webp',t['gallery-exterior'],'large')+tile(t['gallery-interior'],'interior.webp',t['gallery-interior'],'small')+f'''<button type="button" class="gallery-photo gallery-logo" data-open-image="{I}gold-spoon-emblem.webp" data-image-alt="{ex(t['gallery-logo'])}" aria-label="{'Enlarge' if lang=='en' else '확대 보기'}: {ex(t['gallery-logo'])}"><img src="{I}gold-spoon-emblem.webp" alt="{ex(t['gallery-logo'])}" loading="lazy"><figcaption>{t['gallery-logo']} ↗</figcaption></button>'''
 return page_hero(lang,'story')+f'''<section class="story-main"><div class="container"><div class="story-intro"><div class="story-intro-copy reveal"><div class="eyebrow" style="color:var(--auburn)">{t['story-page-intro-kicker']}</div><h2{' class="hangul"' if lang=='ko' else ''}>{t['story-page-intro-title']}</h2><p>{t['story-page-intro-body']}</p>{btn(t['visit-button'],route(lang,'visit'),'ink')}</div><div class="story-intro-photo reveal"><img src="{I}interior.webp" alt="{t['gallery-interior']}" loading="lazy"></div></div><div class="section-heading"><div><div class="eyebrow" style="color:var(--auburn)">{t['gallery-kicker']}</div><h2{' class="hangul"' if lang=='ko' else ''}>{t['gallery-title']}</h2></div><p class="section-sub">{t['gallery-sub']}</p></div><div class="gallery-grid">{gal}</div><div class="gallery-description"><span>{t['gallery-tip']}</span>{btn(t['gallery-yelp'],YELP,'outline-ink',True)}</div></div></section><dialog class="lightbox" data-lightbox aria-label="{'Gallery image' if lang=='en' else '갤러리 이미지'}"><button class="lightbox-close" type="button" data-lightbox-close>{'Close' if lang=='en' else '닫기'} ×</button><img src="{I}storefront.webp" alt=""></dialog>'''

def order_page(lang):
 t=L[lang]
 return page_hero(lang,'order')+f'''<section class="order-main"><div class="container"><div class="order-intro"><div class="eyebrow" style="color:var(--auburn)">{t['order-intro-kicker']}</div><h2{' class="hangul"' if lang=='ko' else ''}>{t['order-intro-title']}</h2><p>{t['order-intro-body']}</p></div><div class="order-grid"><article class="order-card reveal"><span class="order-num">01 /</span><h3>{t['pickup-title']}</h3><p>{t['pickup-body']}</p>{btn(t['pickup-button'],TEL,'red')}</article><article class="order-card reveal"><span class="order-num">02 /</span><h3>{t['delivery-title']}</h3><p>{t['delivery-body']}</p>{btn(t['delivery-button'],DELIVERY,'ink',True)}</article></div><p class="order-footnote">{t['order-note']}</p></div></section><section class="quote-band"><div class="container quote-inner"><h2{' class="hangul"' if lang=='ko' else ''}>{t['quote']}</h2>{btn(t['see-menu'],route(lang,'menu'),'outline-light')}</div></section>'''

def visit_page(lang):
 t=L[lang]
 return page_hero(lang,'visit')+f'''<section class="visit-main"><div class="container visit-grid"><div class="visit-details"><div class="eyebrow" style="color:var(--auburn)">{t['visit-page-kicker']}</div><h2{' class="hangul"' if lang=='ko' else ''}>{t['visit-contact-title']}</h2><div class="detail-group"><label>{t['visit-address-label']}</label><p>{ADDRESS}</p></div><div class="detail-group"><label>{t['visit-phone-label']}</label><a href="{TEL}">{PHONE} ↗</a></div><div class="visit-hours"><h3>{t['visit-hours-label']}</h3>{hours_rows(lang,'visit-hours-row')}<p class="order-footnote" style="margin:15px 0 0">{t['visit-hours-note']}</p></div><div style="margin-top:35px;display:flex;gap:10px;flex-wrap:wrap">{btn(t['visit-map-button'],MAP,'ink',True)}{btn(t['call'],TEL,'outline-ink')}</div></div><div class="map-panel"><iframe title="Gold Spoon Carrollton location on Google Maps" src="https://www.google.com/maps?q=3040+Old+Denton+Rd,+Carrollton,+TX+75007&z=15&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe><div class="map-panel-caption"><span>{t['visit-map-caption']}</span><a href="{MAP}" target="_blank" rel="noopener noreferrer">{t['visit-map-note']} ↗</a></div><div style="margin-top:22px;padding:0 7px 10px"><img src="{I}storefront.webp" alt="{t['gallery-exterior']}" loading="lazy" style="width:100%;height:260px;object-fit:cover"><p style="font-size:11px;color:#b5c1b4;letter-spacing:.05em">{t['gallery-exterior']}</p></div></div></div></section>'''

pages={'home':home,'menu':menu_page,'story':story_page,'order':order_page,'visit':visit_page}
for language in ('en','ko'):
 for page, render in pages.items():
  t=L[language]
  title=('Gold Spoon 금수저 | Korean Dining in Carrollton, TX' if language=='en' else '금수저 Gold Spoon | 캐롤턴 한식당') if page=='home' else f'{t["nav"][page]} | '+('Gold Spoon 금수저' if language=='en' else '금수저 Gold Spoon')
  description=('Visit Gold Spoon Korean restaurant at '+ADDRESS+'. Browse dishes, explore the illustrated dining room, order takeout and find hours.' if language=='en' else '캐롤턴 금수저 한식당. 메뉴와 매장 소개, 주문 안내, 영업시간과 위치를 확인하세요.')
  output=SITE/('ko' if language=='ko' else '')/('' if page=='home' else page)/'index.html'
  output.parent.mkdir(parents=True,exist_ok=True)
  output.write_text(doc(language,page,title,description,render(language)),encoding='utf-8')
  print('created',output.relative_to(ROOT))
