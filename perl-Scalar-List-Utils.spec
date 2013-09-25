%define upstream_name    Scalar-List-Utils
%define upstream_version 1.31
Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	1

Summary:    List utilities (eg min, max, reduce)
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/List/Scalar-List-Utils-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
'List::Util' contains a selection of subroutines that people have expressed
would be nice to have in the perl core, but the usage would not really be
high enough to warrant the use of a keyword, and the size so small such
that being individual extensions would be wasteful.

By default 'List::Util' does not export any subroutines. The subroutines
defined are

* first BLOCK LIST

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.230.0-5
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.230.0-4mdv2011.0
+ Revision: 597100
- rebuild

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 1.230.0-3mdv2011.0
+ Revision: 562428
- rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.230.0-2mdv2011.0
+ Revision: 556140
- rebuild for perl 5.12

* Thu Mar 11 2010 Jérôme Quelin <jquelin@mandriva.org> 1.230.0-1mdv2010.1
+ Revision: 518088
- update to 1.23

* Mon Nov 16 2009 Jérôme Quelin <jquelin@mandriva.org> 1.220.0-1mdv2010.1
+ Revision: 466430
- update to 1.22

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 1.210.0-1mdv2010.0
+ Revision: 395355
- import perl-Scalar-List-Utils


* Sun Jul 12 2009 cpan2dist 1.21-1mdv
- initial mdv release, generated with cpan2dist


