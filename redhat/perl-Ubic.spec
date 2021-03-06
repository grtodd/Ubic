Name:           perl-Ubic
Version:        1.48
Release:        1%{?dist}
Summary:        Polymorphic service manager
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Ubic/
Source0:        http://www.cpan.org/authors/id/M/MM/MMCLERIC/Ubic-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Config)
BuildRequires:  perl(Config::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(HTTP::Server::Simple::CGI)
BuildRequires:  perl(JSON)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(parent)
BuildRequires:  perl(Test::Class)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
Requires:       perl(Class::Accessor::Fast)
Requires:       perl(Config)
Requires:       perl(Config::Tiny)
Requires:       perl(File::Which)
Requires:       perl(HTTP::Server::Simple::CGI)
Requires:       perl(JSON)
Requires:       perl(List::MoreUtils)
Requires:       perl(Params::Validate)
Requires:       perl(parent)
Requires:       perl(Time::HiRes)
Requires:       perl(Try::Tiny)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module is a perl frontend to ubic services.

%prep
%setup -q -n Ubic-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes dist.ini LICENSE README README.md root_t
%{perl_vendorlib}/*
%{_bindir}/ubic
%{_bindir}/ubic-*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Thu Feb 14 2013 Duncan Hutty <dhutty@allgoodbits.org> 1.48-1
- Specfile autogenerated by cpanspec 1.78 with minor modifications
