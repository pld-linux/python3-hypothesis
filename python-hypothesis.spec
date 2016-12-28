#
# Conditional build:
%bcond_without	tests	# test target [nothing to do as of 3.1.0]
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Hypothesis - library for property based testing
Summary(pl.UTF-8):	Hypothesis - biblioteka do testowania opartego na własnościach
Name:		python-hypothesis
Version:	3.1.0
Release:	2
License:	MPL v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/hypothesis/
Source0:	https://pypi.python.org/packages/source/h/hypothesis/hypothesis-%{version}.tar.gz
# Source0-md5:	bddd37c22672dce62e6de315119235d6
URL:		https://github.com/DRMacIver/hypothesis
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-enum34
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
%if "%{py3_ver}" < "3.4"
BuildRequires:	python3-enum34
%endif
%endif
%endif
Requires:	python-modules >= 1:2.7
# for individual -extras modules:
#Suggests:	python-django >= 1.7
#Suggests:	python-fake-factory >= 0.5.2, python-fake-factory <= 0.5.3
#Suggests:	python-numpy >= 1.9.0
#Suggests:	python-pytest >= 2.7.0
#Suggests:	python-pytz
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
Requires:	python3-modules >= 1:3.4
#Suggests:	python3-django >= 1.7
#Suggests:	python3-fake-factory >= 0.5.2, python3-fake-factory <= 0.5.3
#Suggests:	python3-numpy >= 1.9.0
#Suggests:	python3-pytest >= 2.7.0
#Suggests:	python3-pytz

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
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install

%if "%{py3_ver}" >= "3.4"
# avoid python3egg(enum34) dependencies (rpm pythonegg dependency generator
# resolves python version conditions by interpreter used to run the generator)
%{__sed} -i -e "/^\[:python_version == '\(2\.[67]\|3\.3\)'\]/,/^$/d" $RPM_BUILD_ROOT%{py3_sitescriptdir}/hypothesis-%{version}-py*.egg-info/requires.txt
%endif
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