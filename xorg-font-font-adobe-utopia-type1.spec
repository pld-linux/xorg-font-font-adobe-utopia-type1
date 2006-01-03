Summary:	adobe-utopia-type1 font
Summary(pl):	Font adobe-utopia-type1
Name:		xorg-font-font-adobe-utopia-type1
Version:	1.0.1
Release:	0.1
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/font/font-adobe-utopia-type1-%{version}.tar.bz2
# Source0-md5:	aa7ff4bd20b961afda9c15d103b972a5
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	fontconfig
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	t1utils
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/Type1
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
%configure \
	--with-fontdir=%{_fontsdir}/Type1

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# separate *.afm, convert *.pfa to .pfb
cd $RPM_BUILD_ROOT%{_fontsdir}/Type1
install -d afm
mv -f *.afm afm
for f in *.pfa ; do
	t1binary $f `basename $f .pfa`.pfb
	rm -f $f
done
sed -e '1d;s/\.pfa /.pfb /' fonts.scale > fonts.scale.adobe-utopia
rm -f fonts.scale fonts.dir fonts.cache-1

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst Type1

%postun
fontpostinst Type1

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%{_fontsdir}/Type1/*.pfb
%{_fontsdir}/Type1/afm/*.afm
%{_fontsdir}/Type1/fonts.scale.adobe-utopia
