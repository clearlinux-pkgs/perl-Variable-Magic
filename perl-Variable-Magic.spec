#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Variable-Magic
Version  : 0.62
Release  : 15
URL      : https://cpan.metacpan.org/authors/id/V/VP/VPIT/Variable-Magic-0.62.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/V/VP/VPIT/Variable-Magic-0.62.tar.gz
Summary  : 'Associate user-defined magic to variables from Perl.'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Variable-Magic-lib = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Variable::Magic - Associate user-defined magic to variables from Perl.
VERSION
Version 0.62

%package dev
Summary: dev components for the perl-Variable-Magic package.
Group: Development
Requires: perl-Variable-Magic-lib = %{version}-%{release}
Provides: perl-Variable-Magic-devel = %{version}-%{release}

%description dev
dev components for the perl-Variable-Magic package.


%package lib
Summary: lib components for the perl-Variable-Magic package.
Group: Libraries

%description lib
lib components for the perl-Variable-Magic package.


%prep
%setup -q -n Variable-Magic-0.62

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/Variable/Magic.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Variable::Magic.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/auto/Variable/Magic/Magic.so
