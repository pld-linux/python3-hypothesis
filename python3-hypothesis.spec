#
# Conditional build:
%bcond_with	tests	# nothing currently

Summary:	Hypothesis - library for property based testing
Summary(pl.UTF-8):	Hypothesis - biblioteka do testowania opartego na własnościach
Name:		python3-hypothesis
Version:	6.131.20
Release:	1
License:	MPL v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/hypothesis/
Source0:	https://files.pythonhosted.org/packages/source/h/hypothesis/hypothesis-%{version}.tar.gz
# Source0-md5:	ef59cefffce74dc00c7d878bca84349f
URL:		https://github.com/DRMacIver/hypothesis
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-setuptools >= 1:78.1.0
BuildRequires:	python3-wheel
%if %{with tests}
BuildRequires:	python3-attrs >= 19.2.0
%if "%{py3_ver}" == "3.7"
BuildRequires:	python3-importlib_metadata >= 3.6
%endif
BuildRequires:	python3-sortedcontainers >= 2.1.0
BuildRequires:	python3-sortedcontainers < 3.0.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.9
# for individual -extras modules:
#Suggests:	python3-black >= 19.10b0
#Suggests:	python3-click >= 7.0
#Suggests:	python3-dateutil >= 1.4
#Suggests:	python3-django >= 2.2
#Suggests:	python3-dpcontracts >= 0.4
#Suggests:	python3-lark-parser >= 0.6.5
#Suggests:	python3-libcst >= 0.3.16
#Suggests:	python3-numpy >= 1.9.0
#Suggests:	python3-pandas >= 0.25
#Suggests:	python3-pytest >= 4.6
#Suggests:	python3-pytz >= 2014.1
#Suggests:	python3-redis >= 3.0.0
#Suggests:	python3-rich >= 9.0.0
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
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/hypothesis
%{py3_sitescriptdir}/hypothesis
%{py3_sitescriptdir}/_hypothesis_ftz_detector.py
%{py3_sitescriptdir}/_hypothesis_globals.py
%{py3_sitescriptdir}/_hypothesis_pytestplugin.py
%{py3_sitescriptdir}/__pycache__/_hypothesis_ftz_detector.cpython-*.py[co]
%{py3_sitescriptdir}/__pycache__/_hypothesis_globals.cpython-*.py[co]
%{py3_sitescriptdir}/__pycache__/_hypothesis_pytestplugin.cpython-*.py[co]
%{py3_sitescriptdir}/hypothesis-%{version}.dist-info
