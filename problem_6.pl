#!/usr/bin/env perl

# sum of first 100 natural numbers (100)(101)/2
$sum_of_squares=0;
$sum100 = 100*101/2;
$square_of_sum = $sum100 **2;

for ($i=1;$i<101;$i++){
	$sum_of_squares += $i**2;
}

print $sum_of_squares."\n";
print $square_of_sum."\n";
print  $square_of_sum - $sum_of_squares."\n"