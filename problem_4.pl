#!/usr/bin/env perl
# pipe to sort -nr |more tosee largest!

sub id_palindrome {
	$pal = $_[0];
	#print $pal,"\n";
	chomp $pal;
	@digits = split (//, $pal);
	#print @digits;
	#print "\n";
	
	$rev = join ('', reverse @digits);
	
	#print $rev;
	#print "\n";
	print "$pal is a palindrom!!\n" if $pal == $rev
}

for ($i=1000;$i>1;$i--){
	for ($j=1000;$j>1;$j--){
		id_palindrome($i * $j);
	}
}