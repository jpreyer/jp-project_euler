#!/usr/bin/perl
$answer=0;
for ($i=2;$i<1000000;$i++){
	$total=0;
	@a = (split //, $i);
	foreach $j(@a){
		$total += $j**5;
	}

if ($i == $total){
	$answer += $i;
}
}
print "ANSWER : ",$answer,"\n";
