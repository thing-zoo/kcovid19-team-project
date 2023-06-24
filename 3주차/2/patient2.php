<?php
    ini_set('display_errors', '0');
    $link = mysqli_connect("localhost","cathy77","mjwaw4025", "k_covid19"); //이 부분 본인 아이디로 수정
    if( $link === false )
    {
        die("ERROR: Could not connect. " . mysqli_connect_error());
    }
    echo "Coneect Successfully. Host info: " . mysqli_get_host_info($link) . "\n";
?>
<?php
     $state1 = $_POST['state'] ? $_POST['state'] : "*";
?>
<style>
    table {
        width: 100%;
        border: 1px solid #444444;
        border-collapse: collapse;
    }
    th, td {
        border: 1px solid #444444;
    }
</style>
<body>
<h1 style="text-align:center"> 데이터베이스 팀 프로젝트 3주차(1팀) - PatientInfo2 </h1>
<hr style = "border : 5px solid yellowgreen">
    <?php  
    if($state1=="*"){
        $sql = "select count(*) as num from patientinfo";
    }
    else{
        $sql = "select count(*) as num from patientinfo where city='$state1'";
    }
        $result = mysqli_query($link, $sql);
        $data = mysqli_fetch_assoc($result);
    ?>

    <tr>
	<p>state를 선택하세요</p>

<!-- 여기 action부분 php 파일명 각자에 맞게 바꾸기 -->
<form action='patient2.php' name='form1' method='post'> 
<SELECT name='state'>
<?php
     $state1 = $_POST['state'] ? $_POST['state'] : "*";
?>

<?php
     $checking=array();
     $sql = "select * from patientinfo"; //patientinfo를 원하는 테이블 명으로 바꾸기
     $rs = mysqli_query( $link,$sql );

     if( 0 == mysqli_num_rows( $rs ) )
     {
       echo '<OPTION value=""> DB에 문제가 생겼습니다 </OPTION>';
     }
     else
     {
        echo '<OPTION value="*"> city(All State) </OPTION>';//city를 원하는 state로 바꾸기
      while( $r = mysqli_fetch_assoc( $rs ) )
     {
        if(in_array($r['city'], $checking)){} //city말고 원하는 state로 바꾸면 됨
        else{ 
            if(!$r['city']) echo '<OPTION value= NULL> NULL </OPTION>';//city를 원하는 state로 바꾸기
            else echo '<OPTION value=' . $r['city'] . '> ' . $r['city'].'</OPTION>';//city를 원하는 state로 바꾸기
            array_push($checking, $r['city']);
        }
    }
  }
?>
</select>
  <input type='submit' value='submit' />
</form>
</tr>

    <p>
        <h3>PatientInfo table (Currently <?php echo $data['num']; ?>) patients in database </h3>
    </p>

    <table cellspacing="0" width="100%">
        <thead>
        <tr>
            <th>Patient_ID</th>
            <th>Sex</th>
            <th>Age</th>
            <th>Country</th>
            <th>province</th>
            <th>City</th>
            <th>Infection_Case</th>
            <th>Infected_by</th>
            <th>contact_number</th>
            <th>symptom_onset_date</th>
            <th>confirmed_date</th>
            <th>released_date</th>
            <th>deceased_date</th>
            <th>state</th>
        </tr>
        </thead>
        <tbody>
        <?php
	if($state1=="*"){
                $sql = "select * from patientinfo";
    }
    elseif($state1=="NULL"){
        $sql = "select * from patientinfo where city is null";
    }
	else{
                $sql = "select * from patientinfo where city='$state1'";//sql 바꾸기
	}
                $result = mysqli_query($link,$sql);
                while( $row = mysqli_fetch_assoc($result)  )
                {
                    print "<tr>";
                    foreach($row as $key => $val)
                    {
                        print "<td>" . $val . "</td>";
                    }
                    print "</tr>";
                }
            ?>
            
        </tbody>
    </table>


</body>