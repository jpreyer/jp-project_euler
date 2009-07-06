#!/usr/bin/env perl

$n = 1000;
$total=0;

for ($i=1;$i<$n;$i++){
	$rem3 = $i % 3;
	$rem5 = $i % 5;
	if ( ! $rem3 ){
		print "$i is a multiple of 3 ($rem3)\n";
		$total += $i;
	}
	elsif (! $rem5 ){
		print "$i is a multiple of 5 ($rem5)\n";
		$total += $i
	}
}
print "Total is $total\n";
