#!/usr/bin/perl

$n1 = shift;
$n2 = shift;

@digits1 = split (//, $n1);
@digits2 = split (//, $n2);

$dd1 = $digits2[0];
$dd2 = $digits2[1];

foreach $i  (@digits1){
	if ($i == $dd1){
		print "match in 1st digit : $i   $dd1\n";
	}
	if ($i == $dd2){
		print "match in 2nd digit : $i   $dd2\n";
	}
}
