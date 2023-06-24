<?php
    $link = mysqli_connect("localhost","root","mjwaw4025", "k_covid19"); //이 부분 본인 아이디로 수정
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
<body>
    <h1 style="text-align:center"> 데이터베이스 팀 프로젝트 3주차(1팀) - Region </h1>
    <hr style = "border : 5px solid yellowgreen">
    <?php  
        $sql = "select count(*) as num from region ";//sql 바꾸기
        $result = mysqli_query($link, $sql);
        $data = mysqli_fetch_assoc($result);
    ?>

 
    <p>
        <h3>Region table (Currently <?php echo $data['num']; ?>) regions in database </h3>
    </p>

    <table cellspacing="0" width="200%">
        <thead>
        <tr>
            
            <th>region_code</th>
            <th>province</th>
            <th>city</th>
            <th>latitude</th>
            <th>longitude</th>
            <th>elementary_school_count</th>
            <th>kindergarten_count</th>
            <th>university_count</th>
            <th>academy_ratio</th>
            <th>elderly_population_ratio</th>
            <th>elderly_alone_ratio</th>
            <th>nursing_home_count</th>
        </tr>
        </thead>
        <tbody>
            <?php
                $sql = "select * from region";
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