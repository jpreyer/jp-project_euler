#!/usr/bin/env perl

sub seive{


$n = $_[0];
#$n = 600851475143;
#$n = 13195;
$n1 = 2;

$mid = sqrt($n);
print "mid :".$mid."\n";

#ignore 0 and 1...

for ($i=2;$i<$mid;$i++){
	next if $prime[$i] == 2;
	$n1 = 2;
	$prime[$i]=0;
	$j=$n1 * $i;
	while ($j < $n){
		$prime[$j] = 2;
		$n1++;
		$j = $i * $n1;	
	}

}

for ($k=2;$k<$n;$k++){

#	print "counter: $k\n";
	if ($prime[$k] == 0){
		print "$k\n" if ! (87625999  % $k) ;
		$primes{$k} = 2;
		#print "$k\n" ;
	}

}

#foreach $pr (sort  keys %primes){
#	print "$pr\n";
#}
}

$jp = shift;
print seive ( $jp );
