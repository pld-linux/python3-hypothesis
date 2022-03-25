#
# Conditional build:
%bcond_with	tests	# nothing currently

Summary:	Hypothesis - library for property based testing
Summary(pl.UTF-8):	Hypothesis - biblioteka do testowania opartego na własnościach
Name:		python3-hypothesis
Version:	5.49.0
Release:	2
License:	MPL v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/hypothesis/
Source0:	https://files.pythonhosted.org/packages/source/h/hypothesis/hypothesis-%{version}.tar.gz
# Source0-md5:	350fda2e928cc59a38160d9c72f3631c
URL:		https://github.com/DRMacIver/hypothesis
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools >= 1:36.2
%if %{with tests}
BuildRequires:	python3-attrs >= 19.2.0
BuildRequires:	python3-sortedcontainers >= 2.1.0
BuildRequires:	python3-sortedcontainers < 3.0.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
# for individual -extras modules:
#Suggests:	python3-dateutil >= 1.4
#Suggests:	python3-django >= 2.2
#Suggests:	python3-dpcontracts >= 0.4
#Suggests:	python3-lark-parser >= 0.6.5
#Suggests:	python3-numpy >= 1.9.0
#Suggests:	python3-pandas >= 0.25
#Suggests:	python3-pytest >= 4.3
#Suggests:	python3-pytz >= 2014.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hypothesis is a library for testing your Python code against a much
larger range of examples than you would ever want to write by hand.
It's based on the Haskell library, Quickcheck, and is designed to
integrate seamlessly into your existing Python unit testing work flow.

%description -l pl.UTF-8
Hypothesis to biblioteka do testowania kodu w Pythonie względem dużo
większej liczby przykładów, niż kiedykolwiek chciałoby się pisać
ręcznie. Jest oparta na bibliotece Quickcheck języka Haskell i została
zaprojektowana tak, aby w sposób przezroczysty integrowała się z
istniejącym przepływem testów jednostkowych w Pythonie.

%prep
%setup -q -n hypothesis-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{_bindir}/hypothesis
%{py3_sitescriptdir}/hypothesis
%{py3_sitescriptdir}/hypothesis-%{version}-py*.egg-info
