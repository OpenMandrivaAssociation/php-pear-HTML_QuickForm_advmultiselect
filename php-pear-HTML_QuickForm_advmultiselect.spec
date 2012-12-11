%define		_class		HTML
%define		_subclass	QuickForm
%define		upstream_name	%{_class}_%{_subclass}_advmultiselect

Name:		php-pear-%{upstream_name}
Version:	1.5.1
Release:	%mkrel 5
Summary:	Element for HTML_QuickForm that emulate a multi-select
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTML_QuickForm_advmultiselect/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Element for HTML_QuickForm that emulate a multi-select.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{upstream_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/{examples,ChangeLog}
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.5.1-5mdv2012.0
+ Revision: 742001
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.5.1-4
+ Revision: 679352
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5.1-3mdv2011.0
+ Revision: 613678
- the mass rebuild of 2010.1 packages

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.1-2mdv2010.1
+ Revision: 477872
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.1-1mdv2010.0
+ Revision: 383552
- update to new version 1.5.1

* Sun Mar 22 2009 Funda Wang <fwang@mandriva.org> 1.5.0-1mdv2009.1
+ Revision: 360150
- new version 1.5.0

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.4.1-2mdv2009.1
+ Revision: 322119
- rebuild

* Tue Sep 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.1-1mdv2009.0
+ Revision: 278919
- update to new version 1.4.1

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-2mdv2009.0
+ Revision: 236878
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jul 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-1mdv2008.0
+ Revision: 53922
- Import php-pear-HTML_QuickForm_advmultiselect



* Fri Jul 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-1mdv2008.0
- initial Mandriva package
