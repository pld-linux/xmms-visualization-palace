Summary:	Palace - an XMMS visualization used for parallel port light shows
Summary(pl.UTF-8):   Palace - wtyczka dla XMMS-a do sterowania światłami przez port równoległy
Name:		xmms-visualization-palace
Version:	0.2.1
Release:	3
License:	LGPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/palace-dci/palace-%{version}.tar.bz2
# Source0-md5:	d97959c388e3e12bd74e322971ced9c9
URL:		http://palace-dci.sourceforge.net/
BuildRequires:	automake
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
Requires:	xmms
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Palace is a nifty visualization plug in for XMMS. It works by reading
the Fourier frequency analysis given by XMMS, and activating
particular pins on the parallel port based on the frequency analysis
and configuration options. Palace was based on the XPLSISNJASP
software project. For examples of hardware use useful with Palace,
visit one of the following web sites:

http://www.na.linux.hr/projects/xplsisnjasp/ - XPLSISNJASP project web site
http://www.discolitez.com/ - Discolitez is a similar plugin for Winamp

%description -l pl.UTF-8
Palace to wtyczka XMMS-a do sterowania światłami, napisana na bazie
projektu XPLSISNJASP. Dzięki prostemu sprzętowi podłączonemu do
komputera oraz tej wtyczce możemy nasz komputer zamienić w całkiem
przyjemny zestaw do małej domowej dyskoteki :-)

Przykłady sprzętu, który można wykorzystać z Palace, można znaleźć na
tych stronach:

http://www.na.linux.hr/projects/xplsisnjasp/ - strona projektu XPLSISNJASP
http://www.discolitez.com/ - podobna wtyczka dla programu Winamp

%prep
%setup -q -n palace-%{version}

%build
cp -f /usr/share/automake/config.sub .
%configure \
	--datadir=%{xmms_datadir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{xmms_visualization_plugindir} \
	$RPM_BUILD_ROOT%{xmms_datadir}/palace/pixmaps

install ./src/.libs/libpalace.so $RPM_BUILD_ROOT%{xmms_visualization_plugindir}
install ./src/.libs/libpalace.la $RPM_BUILD_ROOT%{xmms_visualization_plugindir}
install ./pixmaps/*.xpm $RPM_BUILD_ROOT%{xmms_datadir}/palace/pixmaps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{xmms_visualization_plugindir}/*
%{xmms_datadir}/*
