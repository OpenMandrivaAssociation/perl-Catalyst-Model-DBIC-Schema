%define upstream_name  	 Catalyst-Model-DBIC-Schema
%define upstream_version 0.26

%define _requires_exceptions perl(Catalyst::Model::DBIC::Schema::Types)

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	DBIx::Class::Schema Model Class 
License:	Artistic/GPL
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Catalyst) >= 5.0
BuildRequires:	perl(DBIx::Class)
BuildRequires:	perl(DBIx::Class::Schema::Loader)
BuildRequires:	perl(DBIx::Class::Cursor::Cached)
BuildRequires:	perl(Catalyst::Devel)
BuildRequires:	perl(CatalystX::Component::Traits)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(Tie::IxHash)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This is a Catalyst Model for DBIx::Class::Schema-based Models. See the
documentation for Catalyst::Helper::Model::DBIC::Schema for information on
generating these Models via Helper scripts.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%__perl Makefile.PL INSTALLDIRS=vendor --skipdeps
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Catalyst
%{_mandir}/*/*
