#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define pnam	SecureState
Summary:	CGI::SecureState - transparent, secure statefulness for CGI programs
Summary(pl):	CGI::SecureState - przezroczysta, bezpieczna obs�uga stanu dla program�w CGI
Name:		perl-CGI-SecureState
Version:	0.36
Release:	1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ccc1f5bbc49c9ee97b0555a0c2dad1b0
BuildRequires:	perl-Crypt-Blowfish
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI:SecureState provides interface to store session data in an
encrypted file on server. Its similar in purpose to CGI::Persistent.

%description -l pl
CGI::SecureState udost�pnia interfejs do przechowywania danych sesji
w zaszyfrowanym pliku na serwerze. Ma podobny cel co CGI::Persistent.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/CGI/SecureState.pm
%{_mandir}/man3/*
