<?php

/* do NOT run this script through a web browser */
if (!isset($_SERVER["argv"][0]) || isset($_SERVER['REQUEST_METHOD'])  || isset($_SERVER['REMOTE_ADDR'])) {
   die("<br><strong>This script is only meant to run at the command line.</strong>");
}

$no_http_headers = true;

include ("/usr/share/cacti/site/include/global.php");
include ("/usr/share/cacti/site/include/config.php");
include ("/usr/share/cacti/site/lib/snmp.php");

$snmp_community = "butler";
$snmp_version = "2";
$hostname[1] = "10.254.2.2";
$hostname[2] = "10.254.2.3";
$hostname[3] = "10.254.2.4";
$hostname[4] = "10.254.2.5";
$interfaceIndex[1] = ".1.3.6.1.4.1.14179.2.1.1.1.38.1";
$interfaceIndex[2] = ".1.3.6.1.4.1.14179.2.1.1.1.38.3";

$newTotal = 0;
$newTotal2 = 0;

for ($x = 1; $x <= 4; $x++) {
    $newArray = cacti_snmp_walk($hostname[$x], $snmp_community, $interfaceIndex[1], $snmp_version, "", "", "", "", "", "", 161, 1000);
    $newArra2 = $newArray["0"];
    $newCount = $newArra2["value"];
    #print $newCount . "\n";
    $newTotal += intval($newCount);
}

for ($x = 1; $x <= 4; $x++) {
    $newArray = cacti_snmp_walk($hostname[$x], $snmp_community, $interfaceIndex[2], $snmp_version, "", "", "", "", "", "", 161, 1000);
    $newArra2 = $newArray["0"];
    $newCount = $newArra2["value"];
    #print $newCount . "\n";
    $newTotal2 += intval($newCount);
}

if ($argv[1] == "secure") {

    print $newTotal . "\n";

}

else {

    print $newTotal2 . "\n";

}
