%define		php_name	php%{?php_suffix}
%define		modname	oggvorbis
%define		status		beta
Summary:	%{modname} - Ogg wrapper for Ogg/Vorbis files
Summary(pl.UTF-8):	%{modname} - wrapper Ogg dla plików Ogg/Vorbis
Name:		%{php_name}-pecl-%{modname}
Version:	0.2
Release:	2
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	b9337dc0a5d024c6b06f68391dc1ea7d
URL:		http://pecl.php.net/package/oggvorbis/
BuildRequires:	libogg-devel >= 2:1.0
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	%{php_name}-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
Obsoletes:	php-pear-%{modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fopen wrapper for Ogg/Vorbis files. Decompress Ogg data to PCM audio
and vice-versa.

In PECL status of this package is: %{status}.

%description -l pl.UTF-8
Wrapper funkcji fopen dla plików Ogg/Vorbis. Dekompresuje Ogg do
formatu PCM audio oraz pozwala na kompresję w drugą stronę.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}
install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
