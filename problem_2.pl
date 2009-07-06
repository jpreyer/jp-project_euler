#!/usr/bin/env perl

sub fib {

# print the nth number in fibonacci sequence

$n = $_[0];
chomp $n;
#print "$n\n";

$f[1] = 1;
$f[2] = 2;

if ($n == 1) {
	return 1;
}
else {
	for ($j=3;$j<=$n;$j++){
		$f[$j] = $f[$j-1] + $f[$j-2];
	}
}


return $f[$n];

}

sub main {
	$count=1;
	$total=0;
	$tt = fib($count);
	while ($tt < 4000000){
		$rem = $tt % 2;
		if (! $rem){
			$total += $tt;
		}
		$tt = fib($count++);
	}
	print "$total\n";
}

main();
