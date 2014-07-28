my ($me,$him) = split(/,/,$ARGV[0]);
if(!defined $me) {
    print "S";
    exit;
}
my $mysharpness =()= ($me =~ /S/g);
$mysharpness -= ($me =~ /P/g);
my $opponentsharpness =()= ($him =~ /S/g);
$opponentsharpness -= ($him =~ /P/g);
if($mysharpness == 0) {
    print "S";
} elsif($opponentsharpness <= 0 || $opponentsharpness == 4) {
    print "P";
} else {
    print "B";
}