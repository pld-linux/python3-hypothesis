#
# Conditional build:
%bcond_with	tests	# nothing currently
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Hypothesis - library for property based testing
Summary(pl.UTF-8):	Hypothesis - biblioteka do testowania opartego na własnościach
Name:		python-hypothesis
Version:	4.57.1
Release:	1
License:	MPL v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/hypothesis/
Source0:	https://files.pythonhosted.org/packages/source/h/hypothesis/hypothesis-%{version}.tar.gz
# Source0-md5:	019caf033d5d5e349141c1cb13860148
URL:		https://github.com/DRMacIver/hypothesis
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools >= 1:36.2
%if %{with tests}
BuildRequires:	python-attrs >= 19.2.0
BuildRequires:	python-coverage >= 4.0
BuildRequires:	python-enum34
BuildRequires:	python-sortedcontainers >= 2.1.0
BuildRequires:	python-sortedcontainers < 3.0.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools >= 1:36.2
%if %{with tests}
BuildRequires:	python3-attrs >= 19.2.0
BuildRequires:	python3-coverage >= 4.0
BuildRequires:	python3-sortedcontainers >= 2.1.0
BuildRequires:	python3-sortedcontainers < 3.0.0
%endif
%endif
Requires:	python-modules >= 1:2.7
# for individual -extras modules:
#Suggests:	python-dateutil >= 1.4
#Suggests:	python-django >= 1.11
#Suggests:	python-dpcontracts >= 0.4
#Suggests:	python-lark-parser >= 0.6.5
#Suggests:	python-numpy >= 1.9.0
#Suggests:	python-pandas >= 0.19
#Suggests:	python-pytest >= 4.3
#Suggests:	python-pytz >= 2014.1
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

%package -n python3-hypothesis
Summary:	Hypothesis - library for property based testing
Summary(pl.UTF-8):	Hypothesis - biblioteka do testowania opartego na własnościach
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5
#Suggests:	python3-dateutil >= 1.4
#Suggests:	python3-django >= 1.11
#Suggests:	python3-dpcontracts >= 0.4
#Suggests:	python3-lark-parser >= 0.6.5
#Suggests:	python3-numpy >= 1.9.0
#Suggests:	python3-pandas >= 0.19
#Suggests:	python3-pytest >= 4.3
#Suggests:	python3-pytz >= 2014.1

%description -n python3-hypothesis
Hypothesis is a library for testing your Python code against a much
larger range of examples than you would ever want to write by hand.
It's based on the Haskell library, Quickcheck, and is designed to
integrate seamlessly into your existing Python unit testing work flow.

%description -n python3-hypothesis -l pl.UTF-8
Hypothesis to biblioteka do testowania kodu w Pythonie względem dużo
większej liczby przykładów, niż kiedykolwiek chciałoby się pisać
ręcznie. Jest oparta na bibliotece Quickcheck języka Haskell i została
zaprojektowana tak, aby w sposób przezroczysty integrowała się z
istniejącym przepływem testów jednostkowych w Pythonie.

%prep
%setup -q -n hypothesis-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/hypothesis
%{py_sitescriptdir}/hypothesis-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-hypothesis
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/hypothesis
%{py3_sitescriptdir}/hypothesis-%{version}-py*.egg-info
%endif
