#!/usr/bin/perl
use strict;
use warnings;
use diagnostics;

## Valid operations
my $SHARPEN = "S";
my $POKE    = "P";
my $BLOCK   = "B";

## It will also print resolution to stderr
my $VERBOSE = 0;

my $first_move = not @ARGV;
my ($me, $you) = split(',', $ARGV[0]) unless( $first_move );

## What do I do?
me_do($SHARPEN, "beginning") if $first_move;
me_do($POKE, "end is near") if  almost_over() || sword($me);
me_do($SHARPEN, "you sword") if !sword($me) && sword($you);
me_do($POKE, "you repeat") if consecutive_sharpens($you) && sharp($me);
me_do(blunt_move(), "you blunt stick") if not sharp($you); 
me_do(aggressive_move(), "me think you sharpen") if sharpen_next($you) && !sharpen_next($me);
me_do($SHARPEN, "me think you block") if you_block_next() && very_little_chance_me_sharpen_next();
me_do($BLOCK, "me have no idea you do");

sub almost_over {
  sharp($me) >= (100 - length($you));
}

sub sharp {
  my $history = shift;
  my $sharp = 0;
  foreach my $s ( split('',$history) ) {
    $sharp++ if( $s eq "S");
    $sharp-- if( $s eq "P" && $sharp > 0);
  }
  return $sharp;
}

sub sword {
  my $me = shift;
  sharp($me) >= 5;
}

sub num_pokes {
  my $me = shift;
  $me =~ s/[^P]//g; #/ SO highlight bug?
  length($me);
}

sub consecutive_sharpens {
  my $you = shift;
  $you =~ m/SS+$/
}

sub sharpen_next {
  my $you = shift;
  $you =~ /([^S]+)S\1S\1$/;
}

sub you_block_next {
  $you =~ /([^B]+B*)B\1B\1$/ || $you =~ /B{4}$/;
}

sub very_little_chance_me_sharpen_next {
  $me !~ /S$/ && ( $me !~ /([^S]+)S\1$/ || $me =~ /^SB+SB+$/ ); 
}

sub blunt_move {
  my $sword_move = sword($me) ? $POKE : $SHARPEN;
  ( $me =~ m/(?:PS){5,}/ || sharp($me)*7 < num_pokes($me) ? $sword_move : aggressive_move() );
}

sub aggressive_move {
  sharp($me)? $POKE : $SHARPEN;
}

sub me_do {
  my ($stick_operation, $reason) = @_;
  my $arg = ( $first_move ? "" : "$me,$you" );
  my $resolution = "$stick_operation me do because $reason ($arg)";
  print "$resolution\n";
  err($resolution);
  exit;
}

sub err {
  my($str) = @_;
  print STDERR "SpeculativeSylwester:$str\n" if $VERBOSE;
}