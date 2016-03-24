<?php

/* do NOT run this script through a web browser */
if (!isset($_SERVER["argv"][0]) || isset($_SERVER['REQUEST_METHOD'])  || isset($_SERVER['REMOTE_ADDR'])) {
   die("<br><strong>This script is only meant to run at the command line.</strong>");
}

$no_http_headers = true;

include ("/usr/share/cacti/site/include/global.php");
include ("/usr/share/cacti/site/include/config.php");
include ("/usr/share/cacti/site/lib/snmp.php");

$fh = fopen("/home/chad/gasbuddy/lastcounter.count",'r+');

$snmp_community = "butler";
$snmp_version = "2";
$hostname = "10.1.0.33";
$interfaceIndex = ".1.3.6.1.2.1.31.1.1.1.6.17";

$lastCount = trim(fgets($fh));
$newArray = cacti_snmp_walk($hostname, $snmp_community, $interfaceIndex, $snmp_version, "", "", "", "", "", "", 161, 1000);
$newArra2 = $newArray["0"];
$newCount = $newArra2["value"];

#print_r($newArray);
#print_r($newCount);

$difference = floatval($newCount) - floatval($lastCount);
$rate = round($difference / 300 * 8 / 1000000,2);

rewind($fh);

ftruncate($fh,0);

fwrite($fh,$newCount);

fclose($fh);

#print "Last: " . $lastCount . " New: " . $newCount . " Difference: " . $difference . " Rate: " . $rate . "\n";
print $rate . "\n";

