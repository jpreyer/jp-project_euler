#!/usr/bin/perl

open F,"<problem11.input" || die "cannot open file";
$i=0;
while (<F>){
	#print ;
	@b = split / /;
	@a[$i] = \@b;
	$i++;
}
print "$a[0]->[6] \n";
