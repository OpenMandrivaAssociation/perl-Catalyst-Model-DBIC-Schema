%define upstream_name  	 Catalyst-Model-DBIC-Schema
%define upstream_version 0.50

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Catalyst::Model::DBIC::Schema::Types\\)'
%else
%define _requires_exceptions perl(Catalyst::Model::DBIC::Schema::Types)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

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


%changelog
* Sun May 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.500.0-1mdv2011.0
+ Revision: 677322
- update to new version 0.50

* Sat May 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.490.0-1
+ Revision: 674569
- fix build dependencies
- update to new version 0.49

* Sat Dec 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.480.0-1mdv2011.0
+ Revision: 620576
- update to new version 0.48

* Wed Dec 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.440.0-1mdv2011.0
+ Revision: 616205
- update to new version 0.44

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.430.0-1mdv2011.0
+ Revision: 561553
- update to 0.43

* Thu Jul 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.410.0-1mdv2011.0
+ Revision: 553577
- update to 0.41

* Fri Feb 05 2010 Jérôme Quelin <jquelin@mandriva.org> 0.400.0-1mdv2010.1
+ Revision: 501141
- update to 0.40

* Tue Feb 02 2010 Jérôme Quelin <jquelin@mandriva.org> 0.390.0-1mdv2010.1
+ Revision: 499483
- update to 0.39

* Fri Jan 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.380.0-1mdv2010.1
+ Revision: 491819
- update to 0.38

* Fri Jan 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.370.0-1mdv2010.1
+ Revision: 491625
- update to 0.37

* Mon Dec 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.350.0-1mdv2010.1
+ Revision: 483035
- update to 0.35

* Mon Nov 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.310.0-2mdv2010.1
+ Revision: 471677
- adding missing requires

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.310.0-1mdv2010.1
+ Revision: 461258
- update to 0.31

* Wed Sep 09 2009 Jérôme Quelin <jquelin@mandriva.org> 0.290.0-1mdv2010.0
+ Revision: 435711
- update to 0.29

* Fri Aug 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.280.0-1mdv2010.0
+ Revision: 421834
- update to 0.28

* Thu Aug 27 2009 Jérôme Quelin <jquelin@mandriva.org> 0.270.0-1mdv2010.0
+ Revision: 421617
- update to 0.27

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.260.0-1mdv2010.0
+ Revision: 408941
- update to 0.26

* Mon Jun 29 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.250.0-2mdv2010.0
+ Revision: 390758
- fix dependencies

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.250.0-1mdv2010.0
+ Revision: 390117
- new version

* Wed Mar 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.23-1mdv2009.1
+ Revision: 353645
- update to new version 0.23

* Wed Mar 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdv2009.1
+ Revision: 348535
- update to new version 0.22

* Sun Aug 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.21-1mdv2009.0
+ Revision: 277942
- update to new version 0.21

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.20-3mdv2009.0
+ Revision: 241155
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-1mdv2008.0
+ Revision: 48056
- fix build dependencies
- update to new version 0.20

* Tue May 08 2007 Buchan Milne <bgmilne@mandriva.org> 0.18-1mdv2008.0
+ Revision: 25041
- Import perl-Catalyst-Model-DBIC-Schema

