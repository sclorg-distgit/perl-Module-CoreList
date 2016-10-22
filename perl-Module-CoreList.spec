%{?scl:%scl_package perl-Module-CoreList}

Name:           %{?scl_prefix}perl-Module-CoreList
# Epoch to compete with perl.spec
Epoch:          1
Version:        5.20160720
Release:        3%{?dist}
Summary:        What modules are shipped with versions of perl
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Module-CoreList/
Source0:        http://www.cpan.org/authors/id/B/BI/BINGOS/Module-CoreList-%{version}.tar.gz
# Avoid loading optional modules from default . (CVE-2016-1238)
Patch0:         Module-CoreList-5.20160720-CVE-2016-1238-avoid-loading-optional-modules-from.patch
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
# File::Copy not used
# Run-time:
# feature not used at tests
# Getopt::Long not used at tests
BuildRequires:  %{?scl_prefix}perl(List::Util)
# Pod::Usage not used at tests
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  %{?scl_prefix}perl(version) >= 0.88
BuildRequires:  %{?scl_prefix}perl(warnings)
# Tests:
BuildRequires:  %{?scl_prefix}perl(Test::More)
# Optional tests:
%if !%{defined perl_bootstrap} && !%{defined perl_small}
BuildRequires:  %{?scl_prefix}perl(Test::Pod) >= 1.00
%endif
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(List::Util)
Requires:       %{?scl_prefix}perl(version) >= 0.88

# Remove under-specified dependencies
%if %{?rhel} < 7
# RPM 4.8 style
%{?filter_setup:
%filter_from_requires /^%{?scl_prefix}perl(version)$/d
%?perl_default_filter
}
%else
# RPM 4.9 style
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(version\\)$
%endif

%description
Module::CoreList provides information on which core and dual-life modules
are shipped with each version of perl.

%package tools
Summary:        Tool for listing modules shipped with perl
Group:          Development/Tools
Requires:       %{?scl_prefix}perl(feature)
Requires:       %{?scl_prefix}perl(version) >= 0.88
Requires:       %{?scl_prefix}perl-Module-CoreList = %{epoch}:%{version}-%{release}
# The files were distributed with perl.spec's subpackage
# perl-Module-CoreList <= 1:5.020001-309
Conflicts:      %{?scl_prefix}perl-Module-CoreList < 1:5.20140914

%description tools
This package provides a corelist(1) tool which can be used to query what
modules were shipped with given perl version.


%prep
%setup -q -n Module-CoreList-%{version}
%patch0 -p1

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tools
%doc README
%{_bindir}/corelist
%{_mandir}/man1/corelist.*

%changelog
* Fri Aug 05 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20160720-3
- Avoid loading optional modules from default . (CVE-2016-1238)

* Thu Jul 21 2016 Petr Pisar <ppisar@redhat.com> - 1:5.20160720-2
- SCL

* Thu Jul 21 2016 Petr Pisar <ppisar@redhat.com> - 1:5.20160720-1
- 5.20160720 bump

* Tue Jun 21 2016 Petr Pisar <ppisar@redhat.com> - 1:5.20160620-1
- 5.20160620 bump

* Mon May 23 2016 Petr Pisar <ppisar@redhat.com> - 1:5.20160520-1
- 5.20160520 bump

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20160507-3
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20160507-2
- Perl 5.24 rebuild

* Tue May 10 2016 Petr Pisar <ppisar@redhat.com> - 1:5.20160507-1
- 5.20160507 bump

* Mon May 02 2016 Petr Pisar <ppisar@redhat.com> - 1:5.20160429-1
- 5.20160429 bump

* Mon Mar 21 2016 Petr Pisar <ppisar@redhat.com> - 1:5.20160320-1
- 5.20160320 bump

* Mon Feb 22 2016 Petr Pisar <ppisar@redhat.com> - 1:5.20160121-1
- 5.20160121 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.20160120-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Petr Pisar <ppisar@redhat.com> - 1:5.20160120-1
- 5.20160120 bump

* Tue Dec 22 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20151220-1
- 5.20151220 bump

* Mon Dec 14 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20151213-1
- 5.20151213 bump

* Mon Nov 23 2015 Petr Pisar <ppisar@redhat.com> - 1:5.20151120-1
- 5.20151120 bump

* Thu Oct 22 2015 Petr Pisar <ppisar@redhat.com> - 1:5.20151020-1
- 5.20151020 bump

* Mon Sep 21 2015 Petr Pisar <ppisar@redhat.com> - 1:5.20150920-1
- 5.20150920 bump

* Mon Sep 14 2015 Petr Pisar <ppisar@redhat.com> - 1:5.20150912-1
- 5.20150912 bump

* Tue Aug 25 2015 Tom Callaway <spot@fedoraproject.org> - 1:5.20150820-1
- 5.20150820 bump

* Tue Jul 21 2015 Petr Pisar <ppisar@redhat.com> - 1:5.20150720-1
- 5.20150720 bump

* Mon Jun 22 2015 Petr Pisar <ppisar@redhat.com> - 1:5.20150620-1
- 5.20150620 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.20150520-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20150520-3
- Perl 5.22 re-rebuild of bootstrapped packages

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.20150520-2
- Perl 5.22 rebuild

* Tue Jun 02 2015 Petr Pisar <ppisar@redhat.com> - 1:5.20150520-1
- 5.20150520 bump

* Tue Apr 21 2015 Petr Pisar <ppisar@redhat.com> - 1:5.20150420-1
- 5.20150420 bump

* Mon Mar 23 2015 Petr Pisar <ppisar@redhat.com> - 1:5.20150320-1
- 5.20150320 bump

* Mon Feb 23 2015 Petr Pisar <ppisar@redhat.com> - 1:5.20150220-1
- 5.20150220 bump

* Mon Feb 16 2015 Tom Callaway <spot@fedoraproject.org> - 1:5.20150214-1
- 5.20150214 bump

* Fri Jan 23 2015 Petr Pisar <ppisar@redhat.com> - 1:5.20150120-1
- 5.20150120 bump

* Fri Jan 02 2015 Petr Pisar <ppisar@redhat.com> - 1:5.20141220-1
- 5.20141220 bump

* Tue Nov 25 2014 Petr Pisar <ppisar@redhat.com> - 1:5.20141120-1
- 5.20141120 bump

* Tue Oct 21 2014 Petr Pisar <ppisar@redhat.com> - 1:5.20141020-1
- 5.20141020 bump

* Wed Oct 08 2014 Petr Pisar <ppisar@redhat.com> - 1:5.20141002-1
- 5.20141002 bump

* Wed Sep 17 2014 Petr Pisar <ppisar@redhat.com> 1:5.20140914-1
- Specfile autogenerated by cpanspec 1.78.
