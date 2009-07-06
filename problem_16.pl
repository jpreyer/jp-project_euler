#!/usr/bin/env perl

sub add_digit{
	$total=0;
	$j = 0;
	$n = $_[0];
	while ($n > 0){
		$d[$j] = $n % 10;
		$n = ($n - $d[$j])/10;
		$j++;
		}
	foreach $p (reverse @d){
		print "$p";
		$total+=$p;
	}
	print "\n";
	print "TOTAL: $total\n";
}

add_digit(2**1000);

print 2**1000 ."\n";
print (2**1000)%100000000000 ."\n";