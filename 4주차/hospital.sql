
CREATE TABLE HOSPITAL(
    hid int, 
    hname varchar(100),
    hprovince varchar(50), 
    hcity varchar(50), 
    hlatitude float(15, 7), 
    hlongitude float(15, 7), 
    capacity int, 
    now int, 
    primary key(hid)
    );

-- patientinfo에 hospital_id 추가 
alter table patientinfo add hospital_id int;