import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    layout='wide',
    initial_sidebar_state='collapsed',
    page_title='대구관광가이드',
    page_icon='🚩'
)


st.sidebar.title('대구 관광지')
menu = st.sidebar.radio('메뉴', options=['테마파크', '자연명소', '피크닉'])

if menu == '테마파크':
    menu1 = st.sidebar.selectbox('선택', options=['이월드', '스파밸리', '대구아쿠아리움'])
if menu == '자연명소':
    menu1 = st.sidebar.selectbox('선택', options=['앞산', '팔공산', '수성못'])
if menu == '피크닉':
    menu1 = st.sidebar.selectbox('선택', options=['대구수목원', '강정보', '달성습지'])







data = [
    {
        'category': '이월드',
        'url': 'https://mblogthumb-phinf.pstatic.net/MjAxNzEyMjlfOTcg/MDAxNTE0NTE5NjQwODAz.nmpj_3eXyLQiGdobkKpPKR-p0Mwtq1KQoqyvRFB50v0g.fwQ4ex4h6I2LX3Bw7sy6NDDrFCkC5au3QLLHyMeENasg.JPEG.llsarull/%EB%8C%80%EA%B5%AC_%EC%9D%B4%EC%9B%94%EB%93%9C_%EB%86%80%EC%9D%B4%EA%B8%B0%EA%B5%AC_%EC%A2%85%EB%A5%98_%EB%AA%A8%EC%9D%8C%2C_%EC%B6%94%EC%B2%9C_%281%29.jpg?type=w800',
        'name': '이월드',
        'content': '대구광역시 달서구 두류공원로 200에 위치한 테마파크. 1995년 개장하였고 우방랜드에서 이월드라는 이름으로 바뀌었다. 대규모 롤러코스터 3개를 동시에 보유하였다. 이외에도 360도 회전하는 놀이기구인 메가스윙, 80m 높이의 스카이드롭이 있다. 대구의 랜드마크 중 하나인 83타워도 이월드 내에 위치한다. 밤이되면 멋진 야경을 볼 수 있고 계절별로 벚꽃축제, 썸머페스티벌 등 다양한 축제가 열린다 ',
        'location': '대구광역시 달서구 두류공원로 200'
    },
    {
        'category': '서문시장',
        'url': 'https://w.namu.la/s/1875612d35fb3e46d8ae3a6a6d4677cb50313b6cb0b751522a0a5507da6b7e796a598ec76e8580fedb7554890012bc5ac00c85108e11039c4f90c2a6ee873096ec91fa7a394b3c1c02f0c771307fbbf5ce8008a036162f3bbbd8689a9a6851f09aa347b12595577e5ddbc50590a0e4d2',
        'name': '서문시장',
        'content': '대구광역시 중구 대신동에 위치한 대구 최대의 전통시장. 대구 뿐만 아니라 전국에서도 손꼽힐 만한 대규모 재래시장이다. 최근에는 서문시장 야시장으로 유명하며, 밤이되면 푸드트럭들이 거리에 줄을 세워 다양한 먹거리를 즐길 수 있다',
        'location': '대구광역시 중구 대신동'
    },


    {
        'category': '팔공산',
        'url': 'https://upload.wikimedia.org/wikipedia/commons/7/72/1%EA%B2%BD_%ED%8C%94%EA%B3%B5%EC%82%B0.jpg',
        'name': '팔공산',
        'content': '파계사, 동화사, 부인사, 송림사, 은해사, 갓바위, 가산산성이 있는 높이 1,193m의 엄청난 규모의 산으로 갓바위, 국립공원, 하늘정원, 한티재, 케이블카 등 다양한 볼거리들이 있다.',
        'location': '대구광역시 동구, 경상북도 경산시, 영천시, 군위군, 칠곡군'
    },
    {
        'category': '앞산',
        'url': 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA5MTRfNDUg%2FMDAxNjYzMTQzOTM0NDM2.j1YwR45ClrrS4LgIFsBpTxk_00hauw4Fb7lAuinkqGwg.cYXmwOqs0ljXs3ohw7VVjvdBgL4hE3mToChI2ruRJAkg.JPEG.kimsh4017%2FKakaoTalk_20220914_172020851_14.jpg&type=sc960_832',
        'name': '앞산',
        'content': '케이블카로 유명하고 전망대로 가면 대구를 한눈에 내려다볼 수 있다. 전망대 시설이 아주 잘 되어있어 계절 상관없이 많은 사람들이 찾아온다',
        'location': '대구광역시 남구 대명동 산227-2'
    },
    {
        'category': '스파밸리',
        'url': 'http://spavalley.co.kr/images/intro/img1_1_1.jpg',
        'name': '스파밸리',
        'content': '대구광역시 달성군 가창면 가창로 891(냉천리 27-27)에 있는 워터파크. 원래는 워터파크지만, 겨울철에는 썰매장으로 운영하기도 한다. 동물원인 네이쳐파크, 온천과 각종 놀이기구들이 있으며 주변에 각종 버스가 다녀서 접근성도 괜찮은 편이다 ',
        'location': '대구광역시 달성군 가창로 891'
    },
    {
        'category': '수성못',
        'url': 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA5MDFfMTk0%2FMDAxNjMwNDg3Mjc0MDg2.Hj9i3znmBQ0z5axqYK2v8GDaiI3db9BXm9jzc7Utf1wg.OBC5E9LuB0SPsRNL0jnmKPTLIVscF_Kyjo9xUpqgxxcg.JPEG.vkfksgksnfl%2FKakaoTalk_20210901_180535138_12.jpg&type=sc960_832',
        'name': '수성못',
        'content': '대구광역시 수성구 무학로 78 (두산동)에 위치한 호수공원. 수성못에서는 오리배를 대여해 탈 수 있고 수성못 옆에는 아르뗴 수성랜드라는 작은 놀이공원이 있으며 매년 9~10월 수성못페스티벌과 분수쇼등 각종 축제가 열린다',
        'location': '대구광역시 수성구 무학로 78'
    },
    {
        'category': '대구아쿠아리움',
        'url': 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA4MjlfMjEg%2FMDAxNjYxNzI4OTE1OTc5.HN8aUM5tt0t7AfSQyHQExxhKYd7BjC7A6Ai500tPZMgg.pYRO5osJILijH2PHcp_FUAsqVPvrkbmqTk-WxvamE_Ug.JPEG.kimgb9600%2F20220827%25A3%25DF110941.jpg&type=sc960_832',
        'name': '대구아쿠아리움',
        'content': '대구신세계 백화점 9층에 위치한 아쿠아리움. 대구지역 최초의 아쿠아리움으로, 다양한 해양생물들이 살고 있다. 마스코트 동물로는 매너티와 홈볼트펭귄이 있다. 수중공연, 버블쇼 등 다양한 이벤트와 공연들이 있다.',
        'location': '대구 동구 동부로 149 신세계백화점 대구점 9층'
    },
    {
        'category': '대구수목원',
        'url': 'https://w.namu.la/s/348fed68bf3edaf5c4ceecdea90fbc40efb7e87c0791c11749fff6e3c497d0bf5ba46cdec4dc40154dfb59708de483c92133cc9a4f111754a81d6340ac41f73f62a8f9f230d14857850b2dc87fc9d384e8a4fc7b204842c5dd4c71e6237004689e2d3a16ffd1774a97d5e805061465cd',
        'name': '대구수목원',
        'content': '대구광역시 달서구 화암로 343에 있는 수목원. 1996년까지 쓰레기 매립장이였던 곳을 수목원으로 조성한 곳이다. 총 21개 주제로 꾸며진 전문 수목원이 있고 깨끗하고 잘 정비되어 있으며 경치도 좋으며 시설도 좋아 여가와 휴식 공간으로는 매우 좋다.',
        'location': '대구광역시 달서구 화암로 343'
    },
    {
        'category': '강정보',
        'url': 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjAzMTFfMTAw%2FMDAxNjQ2OTk4Nzk1Nzk0.WLGSk8z59R5P6pQvU0S8fCceyWC6NpN7VaZ6xMc6rpsg.1IA59A820SKDgcn25eeycIw3aqQ1l0wg71WCaL9IvKYg.JPEG.laondeas%2F3117025201608008k_The_ARC_Cultural_Center.jpg&type=sc960_832',
        'name': '강정보',
        'content': '대구광역시 달성군 다사읍 죽곡리에 걸쳐 있는 낙동강의 보. 디아크라는 고래 모양의 건축물로 유명하며 디아크 내부에는 문화관과 카폐등이 있다. 강변을 따라 자전거나 전동킥보드, 전동바이크등을 대여해 타고다닐 수 있다.',
        'location': '대구광역시 달성군 다사읍 죽곡리'
    },

     {
         'category': '달성습지',
         'url': 'https://korean.visitseoul.net/comm/getImage?srvcId=MEDIA&parentSn=34618&fileTy=MEDIA&fileNo=1&thumbTy=L',
         'name': '달성습지',
         'content': '달성군 다사읍 하빈면부터 다산면 일대까지 형성되어있는 하천습지. 전국 최대 맹꽁이 서식지로도 윰명하다. 산책로가 잘 되어있으며 가을이 되면 갈대받으로도 아주 유명하다.',
         'location': '대구광역시 달성군 다사읍 하빈면'
     }

]
def card_list(menu1):
    result = ''
    for value in data:
        if value['category'] == menu1:
            result = result + f"""
    <div class="col">
    <div class="card" style="width: 60rem;">
        <img src="{value['url']}" class="card-img-top" alt="...">
        <div class="card-body">
        <h5 class="card-title">{value['name']}</h5>
        <p class="card-text">{value['location']}</p>
        </div>
        <ul class="list-group list-group-flush">
        <li class="list-group-item">{value['content']}</li>
            </ul>
        </div>
        </div>
        """

    return result


components.html(
    f"""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>

        <div class="container">
          <div class="row">


             {card_list(menu1=menu1)}
            
      </div>
    </div>

    """, height=1200
)






