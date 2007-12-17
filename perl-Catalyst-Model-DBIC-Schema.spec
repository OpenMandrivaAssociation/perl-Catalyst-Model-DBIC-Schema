%define	module	Catalyst-Model-DBIC-Schema
%define name	perl-%{module}
%define	modprefix Catalyst
%define version 0.20
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	DBIx::Class::Schema Model Class 
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.gz
%if %{mdkversion} < 1010
BuildRequires:	perl-devel >= 5.8.1
%endif
BuildRequires:	perl(Catalyst) >= 5.0
BuildRequires:	perl(DBIx::Class)
BuildRequires:	perl(DBIx::Class::Schema::Loader)
BuildArch:	noarch

%description
This is a Catalyst Model for DBIx::Class::Schema-based Models. See the
documentation for Catalyst::Helper::Model::DBIC::Schema for information on
generating these Models via Helper scripts.

%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/%{modprefix}
%{_mandir}/*/*

%clean
rm -rf %{buildroot}


