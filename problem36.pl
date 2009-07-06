#!/usr/bin/perl

$n1=3;
while ($n1 < 1000000){
$t = 0;
@digits1 = split (//, $n1);
foreach $d (@digits1){
	$j = factorial($d);
	$t += $j
}
if ($t == $n1){
	$sum += $n1;
}
$n1++;
}
print "ANSWER: $sum\n";

sub factorial(){
	$nn = shift;
	$total=1;
	$i=$nn;
	while ($i > 1){
		$total *= $i;
		$i--;
	}
	if ($nn == 0){
		return 1;
	}
	else{
		return $total;
	}
}
