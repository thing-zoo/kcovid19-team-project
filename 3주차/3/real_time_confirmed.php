<?php
    $link = mysqli_connect("localhost","root","mjwaw4025", "k_covid19"); //이 부분 본인 아이디로 수정
    if( $link === false )
    {
        die("ERROR: Could not connect. " . mysqli_connect_error());
    }
    echo "Coneect Successfully. Host info: " . mysqli_get_host_info($link) . "\n";
?>
<?php
$sql = "create view real_time_confirmed as select confirmed_date as date, province, city, infection_case, count(*) as confirmed from patientinfo group by confirmed_date, province, city, infection_case order by confirmed_date desc";
$result = mysqli_query($link,$sql);

$sql = "select * from real_time_confirmed";
$result = mysqli_query($link,$sql);
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
<h1 style="text-align:center"> 데이터베이스 팀 프로젝트 3주차(1팀) - Real Time Confirmed </h1>
<hr style = "border : 5px solid yellowgreen">
<?php  
    $sql = "select count(*) as num from real_time_confirmed";//sql 바꾸기
    $result = mysqli_query($link, $sql);
    $data = mysqli_fetch_assoc($result);
?>


<p>
    <h3>Real Time Confirmed view (Currently <?php echo $data['num']; ?>) Real Time Confirmed datas in database </h3>
</p>

<table cellspacing="0" width="100%">
    <thead>
    <tr>
        <th>date</th>
        <th>province</th>
        <th>city</th>
        <th>infection_case</th>
        <th># of confirmed</th>
    </tr>
    </thead>
    <tbody>
    <?php
            $sql = "select * from real_time_confirmed";
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