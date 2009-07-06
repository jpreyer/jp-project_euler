#!/usr/bin/env perl

open F, "<problem8.input" || die "cannot open input file\n";

while (<F>){
	@a = split //;
}


$ans =0;
for ($i=0;$i<995;$i++){
	$t= $a[$i] * $a[$i+1] *$a[$i+2] * $a[$i+3] *$a[$i+4];
	
	if ($t > $ans){
		$d1=$a[$i];$d2= $a[$i+1]; $d3=$a[$i+2]; $d4=$a[$i+3]; $d5=$a[$i+4];
		$ans = $t;
		
	}
}
print "$d1 * $d2 * $d3 * $d4 * $d5 = $ans\n";