Summary:	Palace is an XMMS visualization used for parallel port light shows.
Summary(pl):	Palace to wtyczka XMMS do sterowania swiatlami przez port rownolegly
Name:		xmms-visualization-palace
Version:	0.2.1
Release:	1
License:	LGPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/palace-dci/palace-%{version}.tar.bz2
# Source0-md5:	d97959c388e3e12bd74e322971ced9c9
URL:		http://palace-dci.sourceforge.net
BuildRequires:	xmms-devel
Requires:	xmms
BuildRoot:	%{tmpdir}/palace-%{version}-root-%(id -u -n)

%define         _xmms_plugin_dir        %(xmms-config --visualization-plugin-dir)
%define         _xmms_data_dir          %(xmms-config --data-dir)

%description
Palace is a nifty visualization plug in for XMMS.  It works by reading the
Fourier frequency analysis given by XMMS, and activating particular pins on
the parallel port based on the frequency analysis and configuration options.
Palace was based on the XPLSISNJASP software project.  For examples of hardware
use useful with Palace, visit one of the following web sites:

http://www.discolitez.com/ - Discolitez is a similar plugin for Winamp

%prep
%setup -q -n palace-%{version} 

%build

%configure --datadir=%{_xmms_data_dir}

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_xmms_plugin_dir} 
install -d $RPM_BUILD_ROOT%{_xmms_data_dir}/palace/pixmaps
install ./src/.libs/libpalace.so $RPM_BUILD_ROOT%{_xmms_plugin_dir}
install ./src/.libs/libpalace.la $RPM_BUILD_ROOT%{_xmms_plugin_dir}
install ./pixmaps/*.xpm $RPM_BUILD_ROOT%{_xmms_data_dir}/palace/pixmaps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_xmms_plugin_dir}/* 
%{_xmms_data_dir}/*
