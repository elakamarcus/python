<?php
header('Content-type: text/html');
$html = file_get_contents("newspage.html");
$date = date("Y-m-d");

/** Currently loading data from plaintext file, consider loading from SQLdb */
$path = "physics";
$html_pieces = explode("<!--==yy==-->", $html);
$html_pieces[0] = str_replace('---$DTA---', $date, $html_pieces[0]);

echo $html_pieces[0];

/* 
 write the Date and time, IP address and User-agent
of visitors to file. After User-Agent, put a separator.
 */
$visit_date = date("Y-m-d h:i:s");

/** Fetch info from text file(s) */
if($fp = fopen($path, "r")){
    while(($row = fgets($fp)) != false ){
        $temp = $html_pieces[1];
        /* $row already hold the first line, subsequent lines
        has to be called with separate fgets(). */
        $temp = str_replace('---$TITLE---', $row, $temp);
        $temp = str_replace('---$DESC---', fgets($fp), $temp);
        $temp = str_replace('---$URL---', fgets($fp), $temp);
        echo $temp;
    }
}
fclose($fp);

echo $html_pieces[2];
?>