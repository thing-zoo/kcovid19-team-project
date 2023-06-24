    
CREATE TABLE TIMEPROVINCE(
	pdate date, 
    province varchar(50), 
    confirmed int(11), 
    released int(11), 
    deceased int(11), 
	PRIMARY KEY (pdate, province)
    );

