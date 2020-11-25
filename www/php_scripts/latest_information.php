<!-- //Scripts to retrieve latest available information -->
<!DOCTYPE html>
<html>
<body>

<?php
function query_latest_lighting($plant_id = "") {
    $query_string_1= "SELECT `DateTime`, ROUND((100*colour_red/colour_total),1) AS relative_red, ROUND((100*`colour_green`/colour_total),1) AS relative_green, ROUND((100*`colour_blue`/colour_total),1) AS relative_blue, `colour_clear` FROM (SELECT `DateTime`, `colour_red`,`colour_green`,`colour_blue`,`colour_clear`, (`colour_red`+`colour_green`+`colour_blue`) AS colour_total FROM `lightsensor_trans` ";
    $query_string_2="";
    $query_string_3= " ORDER BY DateTime DESC LIMIT 1) AS a";

    if $plant_id != "" {
        $query_string_2=" WHERE plant_id=" . $plant_id;
    }

    $query_string_final=$query_string_1 . $query_string_2 . $query_string_3;

    return $query_string_final;
}

echo query_latest_lighting("1");

?>

</body>
</html>