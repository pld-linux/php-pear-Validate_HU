%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_subclass	HU
%define		_status		alpha
%define		_pearname	Validate_HU

Summary:	%{_pearname} - Validation class for Hungary
Summary(pl.UTF-8):	%{_pearname} - Klasa sprawdzająca poprawność dla Węgier
Name:		php-pear-%{_pearname}
Version:	0.1.3
Release:	1
Epoch:		0
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	1e01c41aabf539b08aa9bc7517a19c64
URL:		http://pear.php.net/package/Validate_HU/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.1.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class provides methods to validate:
- Postal code (H-7090, 7090)
- Identity card (123456AA, AA123456)
- Tax number
- Bank account number
- SSN number (TAJ szam)
In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet do sprawdzania poprawności danych takich jak:
- kod pocztowy (H-7090, 7090),
- numer dowodu (123456AA, AA123456),
- numer identyfikacji podatkowej,
- numer konta bankowego,
- numer ubezpieczenia społecznego (TAJ szam)
- numer telefonu

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}.php
