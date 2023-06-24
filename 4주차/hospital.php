<head>
<?php
    $link = mysqli_connect("localhost","cathy77","mjwaw4025", "K_covid19"); //이 부분 본인 아이디로 수정
    if( $link === false )
    {
        die("ERROR: Could not connect. " . mysqli_connect_error());
    }
    echo "Coneect Successfully. Host info: " . mysqli_get_host_info($link) . "\n";
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
<script>
    function openInNewTab(lat, lon) {
        url = "https://www.google.co.kr/maps/search/"+lat;
        url+="+";
        url+=lon;
        var win = window.open(url, 'where_is_hospital', "width=1000, height=1000");
        win.focus();
    }
</script>
</head>
<body>
    <h1 style="text-align:center">  데이터베이스 팀 프로젝트 4주차(1팀) - Hospital </h1>
    <hr style = "border : 5px solid yellowgreen">
    <?php  
        $sql="select count(*) as num from patientinfo";
        $result = mysqli_query($link, $sql);
        $data = mysqli_fetch_assoc($result);
    ?>

    <tr>
   <p>Put Hospital_id</p>

<!-- 여기 action부분 php 파일명 각자에 맞게 바꾸기 -->
<form action='hospital.php' name='form1' method='post'> 

  <input type="text" name='id'/>
  <input type='submit' value='submit' />
<?php 

$state1= isset($_POST['id']) ? $_POST['id'] : "*";
?>
  
</form>
</tr>
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
            <th>hospital_id</th>
        </tr>
        </thead>
        <tbody>
    <?php
   if($state1=="*"){
                $sql = "select * from patientinfo";
                $sql2 = "select hid, hlatitude, hlongitude from hospital";
   }
   else{          
                $sql = "select * from patientinfo where hospital_id='$state1'";//sql 바꾸기
                $sql2 = "select hid, hlatitude, hlongitude from hospital where hid='$state1'";
   }

                $result = mysqli_query($link,$sql);
                $result2 = mysqli_query($link,$sql2);
                $hosparry=[];
                while( $hospit = mysqli_fetch_row($result2)){
                   $hosparry[$hospit[0]]=array($hospit[1],$hospit[2]);
                }
                while( $row = mysqli_fetch_assoc($result))
                {
                    print "<tr>";
                    foreach($row as $key => $val)
                    {
                        if($key == "hospital_id"&&$val != "hospital_id"&&$val != ''){
                            $latti=$hosparry[(int)$val][0];
                            $longi=$hosparry[(int)$val][1];
                            print '<td style="cursor: pointer;" onclick=openInNewTab('.$latti.",".$longi.');>'.$val.'</td>';
                        }
                        else{
                            print "<td>" . $val . "</td>";
                        }
                    }
                    print "</tr>";
                }
    ?>   
    </tbody>
    </table>


</body>