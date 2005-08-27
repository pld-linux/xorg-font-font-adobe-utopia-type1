Summary:	adobe-utopia-type1 font
Summary(pl):	Font adobe-utopia-type1
Name:		xorg-font-font-adobe-utopia-type1
Version:	0.99.0
Release:	0.01
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/font/font-adobe-utopia-type1-%{version}.tar.bz2
# Source0-md5:	05e63b72340f34611de54db6940cb050
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fontconfig
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
adobe-utopia-type1 font.

%description -l pl
Font adobe-utopia-type1.

%prep
%setup -q -n font-adobe-utopia-type1-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/X11/fonts/Type1/*
