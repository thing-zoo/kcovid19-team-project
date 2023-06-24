[4개의 테이블의 의미있는 attribute]

1. PatientInfo의 의미있는 attribute 선정
- patient가 거주하는 city를 선정
- 이유 : patient의 city에서 발생한 정보를 날짜 별로 확인하며 추가적 지역발생에 유의할 수 있다.

2. Region의 의미있는 attribute 선정
- 해당 Region의 city를 선정
- 이유 : Region별로 data를 보았을 때 가장 중요하고 사람들에게 필요한 attribute라고 생각하여 선정하였다.

3. Case의 의미있는 attribute 선정
- 해당 case의 infection_case를 선정
- 이유 : infection_case별 data를 본다면 각각case별 감염정보에 대하여 이해도가 더 높아져 추후 예방책을 강구할 수 있다. 

4. Weather의 의미있는 attribute 선정
- Weather의 날짜 wdate를 선정
- 이유 : 우리가 주로 일별 확진자를 보듯이 일별 날씨에 따라 확진 추세를 확인할 수 있는 용이함이 있다.
