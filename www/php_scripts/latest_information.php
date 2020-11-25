<!-- //Scripts to retrieve latest available information -->
<!DOCTYPE html>
<html>
<body>

<?php
function query_latest_lighting($plant_id, $relative) {
    //Build SQL query string for finding the latest lighting values
    //Optional to provide a specific Plant/Room ID. If left blank, string will find latest value of ANY Plant/Room ID
    $query_string_1="";
    $query_string_2="";
    $query_string_3="";

    $query_string_1relative="SELECT `DateTime`, ROUND((100*colour_red/colour_total),1) AS relative_red, ROUND((100*`colour_green`/colour_total),1) AS relative_green, ROUND((100*`colour_blue`/colour_total),1) AS relative_blue, `colour_clear` FROM (";
    $query_string_1absolute= "SELECT `DateTime`, `colour_red`,`colour_green`,`colour_blue`,`colour_clear`, (`colour_red`+`colour_green`+`colour_blue`) AS colour_total FROM `lightsensor_trans` ";
    
    $query_string_3absolute= " ORDER BY DateTime DESC LIMIT 1";
    $query_string_3relative=") AS a";

    if $plant_id != "" {
        $query_string_2=" WHERE plant_id=" . $plant_id;
    }

    if $relative==true{
        $query_string_1=$query_string_1relative . $query_string_1absolute;
        $query_string_3=$query_string_3absolute . $query_string_3relative;
    } else {
        $query_string_1=$query_string_1absolute;
        $query_string_3=$query_string_3absolute;
    }

    $query_string_final=$query_string_1 . $query_string_2 . $query_string_3;

    return $query_string_final;
}

function fetch_latest_lighting($plant_id = "", $relative=false){
    //Get latest lighting values for Plant/Room ID provided
    $sql_string=query_latest_lighting($plant_id);

    $latest_lighting = $wpdb->get_results($sql_string);
    return $latest_lighting;
}

echo fetch_latest_lighting("1",false);

?>

</body>
</html>