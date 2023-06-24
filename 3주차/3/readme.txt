[의미있는 view]

1조는 patientinfo의 4개의 attribute(confirmed_date, province, city , infection_case)와 이들을 grouping하여 count(*)를 통해 산출한 확진자수까지 총 5개의 attribute을 포함하고 confirmed_date를 기준으로 내림차순 정렬되는 view를 만들었다.

view의 attributes: confirmed_date as date, province, city , infection_case, count(*) as confirmed(확진자 수)


- 설명 : 해당하는 날짜에 어떤 도시에서 어떤 감염 경우로 확진 되었다. 그리고 그에 대한 확진자 수는 00명이다.
예) 2020-6-30 충첨남도 부여군에서 해외유입으로 확진자 1명이 발생하였다.

날짜는 최근날짜순으로 정렬을 하여 최신의 정보를 바로 확인가능하다.
날짜별로 해당 날짜에 감염정보를 통하여 사태의 진행성이 확인가능하다.
이를 바탕으로 현 사태의 문제점과 대책을 강구해야할 부분에 대한 기반을 만들 수 있다.