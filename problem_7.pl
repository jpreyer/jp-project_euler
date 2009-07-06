#!/usr/bin/env perl

sub seive{


$n = $_[0];
#$n = 600851475143;
#$n = 13195;
$n1 = 2;

$mid = sqrt($n);
#print "mid :".$mid."\n";

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

	if ($prime[$k] == 0){
		$primes{$k} = 2;
	}

}

$primecount =0;
foreach $pr ( sort { $a <=> $b } keys %primes){
	$primecount++;
	print "$pr\n" if $primecount == 10001;
}
}

$jp = 200000;
print seive ( $jp );
