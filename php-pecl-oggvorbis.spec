%define		_modname	oggvorbis
%define		_status		beta
Summary:	%{_modname} - Ogg wrapper for Ogg/Vorbis files
Summary(pl):	%{_modname} - wrapper Ogg dla plików Ogg/Vorbis
Name:		php-pecl-%{_modname}
Version:	0.2
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	b9337dc0a5d024c6b06f68391dc1ea7d
URL:		http://pecl.php.net/package/oggvorbis/
BuildRequires:	libogg-devel >= 2:1.0
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	php-devel
Requires:	php-common
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
Fopen wrapper for Ogg/Vorbis files. Decompress Ogg data to PCM audio
and vice-versa.

In PECL status of this package is: %{_status}.

%description -l pl
Wrapper funkcji fopen dla plików Ogg/Vorbis. Dekompresuje Ogg do
formatu PCM audio oraz pozwala na kompresjê w drug± stronê.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
