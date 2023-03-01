Summary:	Adobe Utopia Type1 font
Summary(pl.UTF-8):	Font Type1 Adobe Utopia
Name:		xorg-font-font-adobe-utopia-type1
Version:	1.0.5
Release:	1
License:	distributable (see COPYING)
Group:		Fonts
Source0:	https://xorg.freedesktop.org/releases/individual/font/font-adobe-utopia-type1-%{version}.tar.xz
# Source0-md5:	546d17feab30d4e3abcf332b454f58ed
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	fontconfig
BuildRequires:	t1utils
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.2
BuildRequires:	xorg-util-util-macros >= 1.20
BuildRequires:	xz
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/Type1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Adobe Utopia Type1 font.

%description -l pl.UTF-8
Font Type1 Adobe Utopia.

%prep
%setup -q -n font-adobe-utopia-type1-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
%if "%{_gnu}" != "-gnux32"
	--build=%{_host} \
	--host=%{_host} \
%endif
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
cat > Fontmap.adobe-utopia <<EOF
/Utopia-BoldItalic                       (UTBI____.pfb) ;
/Utopia-Bold                             (UTB_____.pfb) ;
/Utopia-Italic                           (UTI_____.pfb) ;
/Utopia-Regular                          (UTRG____.pfb) ;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst Type1

%postun
fontpostinst Type1

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%{_fontsdir}/Type1/UT*.pfb
%{_fontsdir}/Type1/afm/UT*.afm
%{_fontsdir}/Type1/fonts.scale.adobe-utopia
%{_fontsdir}/Type1/Fontmap.adobe-utopia
