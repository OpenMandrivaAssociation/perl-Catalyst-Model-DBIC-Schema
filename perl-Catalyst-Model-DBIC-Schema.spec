%define upstream_name  	 Catalyst-Model-DBIC-Schema
%define upstream_version 0.62

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Catalyst::Model::DBIC::Schema::Types\\)'
%else
%define _requires_exceptions perl(Catalyst::Model::DBIC::Schema::Types)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	DBIx::Class::Schema Model Class 
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst) >= 5.0
BuildRequires:	perl(Catalyst::Devel)
BuildRequires:	perl(CatalystX::Component::Traits)
BuildRequires:	perl(Class::C3)
BuildRequires:	perl(DBIx::Class)
BuildRequires:	perl(DBIx::Class::Schema::Loader)
BuildRequires:	perl(DBIx::Class::Cursor::Cached)
BuildRequires:	perl(Module::Find)
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Tie::IxHash)
Requires:	perl(CatalystX::Component::Traits)
BuildArch:	noarch

%description
This is a Catalyst Model for DBIx::Class::Schema-based Models. See the
documentation for Catalyst::Helper::Model::DBIC::Schema for information on
generating these Models via Helper scripts.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor --skipdeps
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Catalyst
%{_mandir}/*/*
