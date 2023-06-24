USE K_COVID19;

drop TABLE TimeGender;

CREATE TABLE TimeGender(
	gdate date,
    sex varchar(10),
    confirmed int,
    deceased int,
    PRIMARY KEY(gdate, sex)
	);