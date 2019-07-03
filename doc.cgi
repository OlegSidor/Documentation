#!/usr/bin/perl
=head1 NAME

 Abills doc

=cut

use strict;
use warnings;

BEGIN {
  our $libpath = '../';
  my $sql_type = 'mysql';
  unshift(@INC,
    $libpath . "Abills/$sql_type/",
    $libpath . "Abills/modules/",
    $libpath . '/lib/',
    $libpath . '/Abills/',
    $libpath
  );
}

our (
  $libpath,
  %conf,
  %FORM,
);

do "../libexec/config.pl";


use Abills::HTML;
my $html = Abills::HTML->new(
  {
    IMG_PATH => 'img/',
    NO_PRINT => 1,
    CONF     => \%conf,
    CHARSET  => $conf{default_charset},
  }
);

use Abills::SQL;
my $db = Abills::SQL->connect($conf{dbtype}, $conf{dbhost}, $conf{dbname}, $conf{dbuser}, $conf{dbpasswd}, {
  CHARSET => ($conf{dbcharset}) ? $conf{dbcharset} : undef
});

print $html->header();
if ($FORM{url}) {
  use Doc::db::Documentation;
  my $Doc = Documentation->new($db, undef, \%conf);
  my $url = $Doc->list({
    WIKI       => $FORM{url},
    CONFLUENCE => '_SHOW',
    COLS_NAME  => 1
  });
  $url = $url->[0]->{confluence} if($url);
  $url = 'http://abills.net.ua:8090' if(!$url);

  $html->redirect($url);
}
1;