%define		_class		HTML
%define		_subclass	QuickForm
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}_advmultiselect

Summary:	%{_pearname} - Element for HTML_QuickForm that emulate a multi-select
Name:		php-pear-%{_pearname}
Version:	1.4.0
Release:	%mkrel 1
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/HTML_QuickForm_advmultiselect/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Element for HTML_QuickForm that emulate a multi-select.

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}
install -d %{buildroot}%{_datadir}/pear/data/%{_pearname}

install -m0644 %{_pearname}-%{version}/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/
install -m0644 %{_pearname}-%{version}/*.js %{buildroot}%{_datadir}/pear/data/%{_pearname}/

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

perl -pi -e "s|\@data_dir\@|%{_datadir}/pear/data|g" %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/*.php
perl -pi -e "s|\@package_name\@|%{_pearname}|g" %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/*.php

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{docs,examples,ChangeLog,NEWS}
%{_datadir}/pear/%{_class}/%{_subclass}/*.php
%dir %{_datadir}/pear/data/%{_pearname}
%{_datadir}/pear/data/%{_pearname}/*.js
%{_datadir}/pear/packages/%{_pearname}.xml
